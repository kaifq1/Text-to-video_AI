import os, torch, numpy as np
from safetensors.torch import load_file
from diffusers import AnimateDiffPipeline, MotionAdapter, EulerDiscreteScheduler
from PIL import Image
import ffmpeg
import tempfile

def load_pipeline(adapter_path="/content/AnimateDiff-Lightning"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device=="cuda" else torch.float32
    step = 4

    ckpt = os.path.join(adapter_path, f"animatediff_lightning_{step}step_diffusers.safetensors")
    adapter = MotionAdapter().to(device, dtype)
    adapter.load_state_dict(load_file(ckpt, device=device))

    base = "emilianJR/epiCRealism"
    pipe = AnimateDiffPipeline.from_pretrained(base, motion_adapter=adapter, torch_dtype=dtype).to(device)
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing", beta_schedule="linear")
    pipe.enable_model_cpu_offload(); pipe.enable_attention_slicing()
    return pipe, step

def frames_to_video(frames, fps, out_path):
    with tempfile.TemporaryDirectory() as td:
        for i, f in enumerate(frames):
            Image.fromarray(f).save(f"{td}/frame_{i:05d}.png")
        (
            ffmpeg
            .input(f"{td}/frame_%05d.png", framerate=fps)
            .output(out_path, pix_fmt="yuv420p", vcodec="libx264")
            .overwrite_output().run(quiet=True)
        )

def generate_segments(pipe, step, prompts, fps=6):
    segs = []
    for idx, p in enumerate(prompts):
        print(f"→ Generating segment {idx+1}/{len(prompts)}")
        out = pipe(prompt=p, guidance_scale=1.0, num_inference_steps=step)
        frames = [np.array(f) for f in out.frames[0]]
        vid = f"seg_{idx}.mp4"
        frames_to_video(frames, fps, vid)
        segs.append((vid, p))
        torch.cuda.empty_cache()
    return segs
