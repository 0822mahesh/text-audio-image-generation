import os
import google.generativeai as genai
import streamlit as st
from  PIL import Image
from dotenv import load_dotenv
import mimetypes

load_dotenv()

st.title("Audio to text Conversion")
st.sidebar.header(" Upload Audio File")
audio_file = st.sidebar.file_uploader("Upload an Audio file", type=["MP3", "MVC","ALAC"])


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

if audio_file:
    try:
        
        mime_type, _ = mimetypes.guess_type(audio_file.name)
        audio_file1 = genai.upload_file(audio_file,mime_type=mime_type)
       
        promt = "Listen the audio file and provide brif summry information"
      
        llm = genai.GenerativeModel("gemini-1.5-flash")
        response = llm.generate_content([promt, audio_file1])
        
       
        st.subheader("AI Response")
        st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please upload an audio file to get started.")