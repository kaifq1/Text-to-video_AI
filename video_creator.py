

import streamlit as st
import os
from preprocessing import clear_context_only
from model import load_pipeline, generate_segments
from audio import generate_audio, list_available_models
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

def show_video_creator_ui():
    st.title("🎬 NarrativeFrames: Create Your Story Video")

    # Voice model selection
    model_choice = st.selectbox("🎙️ Choose Voice Model", list_available_models())

    # Story input
    story = st.text_area("📝 Enter your story:", height=200)

    if st.button("🚀 Start Generating"):
        if not story.strip():
            st.warning("⚠️ Please enter a story.")
            return

        # Preprocessing
        st.info("🔍 Extracting prompts...")
        prompts = clear_context_only(story)
        for i, p in enumerate(prompts):
            st.markdown(f"**{i+1}.** {p}")

        # Load animation model
        st.info("⏳ Loading animation pipeline...")
        pipe, step = load_pipeline()
        st.success("✅ Model loaded.")

        segments = []

        # Generate segments
        for i, prompt in enumerate(prompts):
            st.markdown(f"### 🎞️ Segment {i+1}")
            st.text(f"Processing:\n{prompt}")

            # Generate video
            vid_path, _ = generate_segments(pipe, step, [prompt])[0]

            # Generate audio
            audio_path, _ = generate_audio(prompt, model_key=model_choice)

            # Merge video and audio
            merged = f"merged_{i}.mp4"
            vc = VideoFileClip(vid_path)
            ac = AudioFileClip(audio_path)
            final = vc.set_audio(ac)
            final.write_videofile(merged, fps=vc.fps, codec="libx264", audio_codec="aac", verbose=False, logger=None)
            segments.append(merged)

        # Concatenate all segments
        st.info("🎞️ Concatenating all segments...")
        clips = [VideoFileClip(p) for p in segments]
        out = "final_story.mp4"
        final_video = concatenate_videoclips(clips, method="compose")
        final_video.write_videofile(out, fps=clips[0].fps, codec="libx264", audio_codec="aac", verbose=False, logger=None)

        # Show results
        st.success("✅ Done! Your video is ready.")
        st.video(out)
        with open(out, "rb") as f:
            st.download_button("⬇️ Download Final Video", data=f, file_name="final_story.mp4", mime="video/mp4")

        # Cleanup
        for path in segments:
            os.remove(path)

# EOF
