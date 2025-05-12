
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

```
---

## 🚀 Usage

### 🔹 Launch the Streamlit App

```bash
streamlit run streamlit_app.py
```
🏠 Home Page
- Click on "Create Video" to open the video creation interface.

🎨 Creator Interface
- Paste your narrative/script into the text box.

Adjust the following settings:

- Segment Count – Number of segments the story is split into.

- Inference Steps – Affects the video quality and generation time.

- Audio Voice – Choose from available TTS voices.

Click "Generate Video" and wait while the AI pipeline processes your input.

Once done, preview the video and download your final output.

🌐 Public Sharing (via ngrok)
- After launching, ngrok will provide a public URL in the terminal.

Share this link with others to showcase your app in real-time.

---

## 📬 Contact
For suggestions, collaborations, or questions:

📧 kaifq125@gmail.com

🔗 www.linkedin.com/in/kaif-qureshi-989b1b246


--
## 📄 License

This project is licensed under the [MIT License].
