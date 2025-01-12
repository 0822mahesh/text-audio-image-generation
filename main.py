import os
import streamlit as st 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    pages= {
        " Text generation ": [st.Page("app.py",title="Text to text")],
        "Image to Text": [st.Page("image_text.py",title="image to text")],
        "audio to Text": [st.Page("audio_text.py",title="Audio to text")]
        }
        
    pg=st.navigation(pages)
    pg.run()



if __name__ == "__main__":
    main()
