import os
import google.generativeai as genai
import streamlit as st
from  PIL import Image
from dotenv import load_dotenv

load_dotenv()

st.title("Image to text conersion")
st.sidebar.header(" Upload immage")
image_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "png"])
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

if image_file:
    try:
        # Load the uploaded image
        image = Image.open(image_file)
       # st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract text from the image using OCR
        

        # Process the extracted text with Generative AI
        llm = genai.GenerativeModel("gemini-1.5-flash")
        response = llm.generate_content(["Tell me about this ", image])
        
        # Display the AI-generated response
        st.subheader("AI Response")
        st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please upload an image to get started.")


# llm = genai.GenerativeModel("gemini-1.5-flash")


# model = genai.GenerativeModel("gemini-1.5-flash")
# organ = Image.open(image_file)
# response = model.generate_content(["Tell me about this ", organ])
# print(response.text)
# st.write(response.text)