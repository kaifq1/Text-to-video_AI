
# 🎬 Narrative Frames – Text to Video Generation

Narrative Frames is a creative AI-powered tool that transforms written stories into engaging, animated videos. Built using diffusion models, TTS pipelines, and Streamlit, it brings imagination to life—frame by frame.

Developed by **Kaif**, **Vinit Jethwa**, and **Sachin Singh**, this project showcases the blend of storytelling, generative AI, and open-source innovation.

---

## 🚀 Features

- ✍️ **Story Preprocessing**  
  Breaks down text into structured narrative elements using NLP techniques.

- 🧠 **AI-Powered Video Generation**  
  Converts each story element into a short animated clip using AnimateDiff and MotionAdapter.

- 🔊 **Text-to-Speech Narration**  
  Uses Coqui TTS to narrate the story, matching the visuals with human-like audio.

- 🎞️ **Video Stitching & Final Output**  
  Automatically syncs video clips and narration into a smooth, cinematic final video.

---

## 🧰 Tech Stack

- Python 3.8+
- Streamlit
- AnimateDiff + MotionAdapter
- Coqui TTS
- PyTorch, OpenCV, PIL

---

## 🗂️ Project Structure

```bash
📁 Narrative-Frames
├── streamlit_app.py             # Main Streamlit application
├── preprocessing.py             # Text cleaning and segmentation
├── model.py                     # Diffusion model pipeline and setup
├── audio.py                     # Narration synthesis and audio processing
├── video_creator.py             # Frame generation and video composition
├── Narrative_Frames_Test_to_Video.ipynb  # Jupyter demo notebook
├── requirements.txt.txt         # Dependency list
