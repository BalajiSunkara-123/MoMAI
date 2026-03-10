import streamlit as st
import tempfile

from modules.speech_to_text import transcribe_audio
# from modules.summarizer_finetuned import summarize_text
from modules.summarizer_pretrained import summarize_text
from modules.structure_minutes import structure_minutes

st.set_page_config(page_title="AI Meeting Minutes Generator")

st.title("🎤 AI Meeting Minutes Generator")

st.write("Upload a meeting audio file and generate structured meeting minutes.")

uploaded_file = st.file_uploader("Upload Meeting Audio", type=["wav","mp3","m4a"])


if uploaded_file is not None:

    st.audio(uploaded_file)

    if st.button("Generate Minutes"):

        with st.spinner("Processing audio..."):

            # save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(uploaded_file.read())
                audio_path = tmp.name

            # Step 1: Speech to text
            transcript = transcribe_audio(audio_path)

            st.subheader("Transcript")
            st.write(transcript)

            # Step 2: Summarization
            summary = summarize_text(transcript)

            st.subheader("Summary")
            st.write(summary)

            # Step 3: Structured Minutes
            minutes = structure_minutes(summary)

            st.subheader("Meeting Minutes")
            st.text(minutes)