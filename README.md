# Narrative-Frames-Text-to-video-generation


**🎬 Narrative Frames: Text-to-Video Storytelling**

Welcome to **Narrative Frames**, a Streamlit‑powered application that transforms your written narrative into a dynamic, animated video. Harnessing the power of AnimateDiff, MotionAdapter, and advanced audio pipelines, you can turn any text prompt into a polished video story in minutes.

Developed by **Kaif Qureshi**, **Vinit Jethwa**, and **Sachin Singh**, this project showcases the blend of storytelling, generative AI, and open-source innovation.

---

## 🔎 Features

* **Text Preprocessing**: Clean and extract core story segments using `preprocessing.py` (pronoun stripping, NP extraction).
* **Diffusion‑based Video Generation**: Load and run the ByteDance AnimateDiff‑Lightning pipeline to generate per‑segment video clips.
* **Audio Synthesis**: Generate narration audio with Coqui TTS and synchronize it with video frames.
* **Streamlit UI**: Intuitive web interface (`streamlit_app.py`) to upload scripts, preview segments, and download final MP4.
* **Automatic Deployment**: Built‑in support for ngrok tunnels to share your local app publicly.

---

## 📁 Repository Structure

```bash
├── preprocessing.py       # Text cleaning & segment extraction
├── model.py               # Load AnimateDiff pipeline & segment renderer
├── video_creator.py       # Core stitching logic: combine clips + audio
├── streamlit_app.py       # Streamlit front‑end UI & navigation
├── requirements.txt       # Pinpointed Python dependencies
└── README.md              # This documentation
```

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/narrative-frames.git
   cd narrative-frames
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

3. **Clone AnimateDiff‑Lightning**

   ```bash
   git clone https://huggingface.co/ByteDance/AnimateDiff-Lightning AnimateDiff-Lightning
   ```

4. **Prepare ngrok (optional)**

   ```bash
   pip install pyngrok
   export NGROK_AUTH_TOKEN="<YOUR_NGROK_TOKEN>"
   ```

---

## 🚀 Usage

1. **Launch the Streamlit app**

   ```bash
   streamlit run streamlit_app.py
   ```

2. **Home Page**

   * Click **"Create Video"** to navigate to the creator interface.

3. **Creator Interface**

   * Paste your narrative script.
   * Adjust **segment count**, **inference steps**, and **audio voice**.
   * Click **"Generate Video"** and wait for the pipeline to finish.
   * Preview and **download** your final video.

4. **Public Share (ngrok)**

   * After launch, ngrok will output a public URL: share this link to demo your app in real‑time.

---

## 🛠️ Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request on GitHub.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
