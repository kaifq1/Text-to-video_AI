import os, tempfile, re
from TTS.api import TTS
import soundfile as sf
from pydub import AudioSegment

# Regex to split on sentence boundaries
_SENT_RE = re.compile(r'(?<=[\\.\\!?]) +')

# Pre-defined models you can choose from:
AVAILABLE_MODELS = {
    "LJSpeech VITS":         "tts_models/en/ljspeech/vits",
    "Tacotron2-DDC":         "tts_models/en/ljspeech/tacotron2-DDC",
    "VCTK VITS":             "tts_models/en/vctk/vits",
    # Add more model keys ↔ HF IDs here…
}

def list_available_models():
    """Return human-readable model names."""
    return list(AVAILABLE_MODELS.keys())

def generate_audio(
    text: str,
    model_key: str = "LJSpeech VITS",
    speaker: str = None,
    language: str = None
) -> (str, list):
    """
    Generate speech for the given text.

    Args:
      text: full input text.
      model_key: key from AVAILABLE_MODELS.
      speaker: optional (for multi-speaker models).
      language: optional (for multilingual models).

    Returns:
      final_wav: path to the concatenated WAV file.
      timeline: list of (sentence, start_time, duration).
    """
    if model_key not in AVAILABLE_MODELS:
        raise ValueError(f"Unknown model '{model_key}'. Choose from {list_available_models()}")

    model_name = AVAILABLE_MODELS[model_key]
    tmpdir = tempfile.mkdtemp()

    # Split text into sentences
    sentences = _SENT_RE.split(text.strip())
    if not sentences:
        raise ValueError("No valid sentences found in text.")

    # Initialize TTS engine (no speaker/language here)
    tts = TTS(model_name=model_name)

    segs, timeline, current = [], [], 0.0
    for i, sent in enumerate(sentences, 1):
        out_path = os.path.join(tmpdir, f"seg_{i}.wav")
        # Pass speaker/language to tts_to_file
        tts.tts_to_file(text=sent, file_path=out_path,
                        speaker=speaker, language=language)
        data, sr = sf.read(out_path)
        dur = len(data) / sr

        segs.append(AudioSegment.from_wav(out_path))
        timeline.append((sent, current, dur))
        current += dur

    # Concatenate segments
    final_wav = os.path.join(tmpdir, "output.wav")
    combined = segs[0]
    for seg in segs[1:]:
        combined += seg
    combined.export(final_wav, format="wav")

    return final_wav, timeline
