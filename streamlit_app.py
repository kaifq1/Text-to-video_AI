import streamlit as st
from PIL import Image

# Session state to manage page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to_creator():
    st.session_state.page = "creator"

if st.session_state.page == "home":
    st.set_page_config(page_title="🎬 Narrative Frames", layout="centered")
    st.title("🎬 Narrative Frames")
    st.markdown("#### Transform your text into compelling video stories.")

    st.markdown("""
    **Narrative Frames** is an AI-powered text-to-video storytelling platform.
    Just enter a story, and we generate beautiful animated visuals, synced with lifelike narration.
    Perfect for educators, creators, and storytellers!
    """)

    st.divider()
    st.subheader("👨‍💻 Meet the Team")

    col1, col2, col3 = st.columns(3)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("/content/drive/MyDrive/Narrative_Frames/Vinit_jethwa.jpeg", caption="", use_container_width=True)
        st.markdown('<div style="text-align: center;"><strong>Vinit Jethwa</strong></div>', unsafe_allow_html=True)

    with col2:
        st.image("/content/drive/MyDrive/Narrative_Frames/sachin_singh.jpeg", caption="", use_container_width=True)
        st.markdown('<div style="text-align: center;"><strong>Sachin Singh</strong></div>', unsafe_allow_html=True)

    with col3:
        st.image("/content/drive/MyDrive/Narrative_Frames/kaif_qureshi.jpeg", caption="", use_container_width=True)
        st.markdown('<div style="text-align: center;"><strong>Kaif Qureshi</strong></div>', unsafe_allow_html=True)


    st.divider()
    st.markdown("### 🚀 Ready to create your story?")
    if st.button("Start", key="start_button"):
        go_to_creator()

elif st.session_state.page == "creator":
    from video_creator import show_video_creator_ui
    show_video_creator_ui()
