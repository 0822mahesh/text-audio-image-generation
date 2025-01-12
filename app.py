import os
import streamlit as st 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#google_api_key = os.getenv("GOOGLE_API_KEY")


def get_api_keys():
    return os.getenv("GOOGLE_API_KEY"), os.getenv("OPENAI_API_KEY")

def render_sidebar():
    st.sidebar.title("Settings")
    st.sidebar.subheader("API Keys")
    model = st.sidebar.selectbox("Model",("Google", "OpenAI"))
    temparature = st.sidebar.slider("Temparature",min_value=0.0,max_value=1.0,value=0.7)
    max_tokens = st.sidebar.slider("Max Tokens",min_value=10,max_value=150,value=50)

    return model, temparature, max_tokens


def handle_query(model,query,max_tokens,temp):
    google_api_key, openai_api_key = get_api_keys()
    if model == "Google":
        llm = ChatGoogleGenerativeAI(api_key=google_api_key, model="gemini-1.5-pro-latest",max_tokens=max_tokens,temperature=temp)
    elif model == "OpenAI":
        llm = ChatOpenAI(model = "gpt-4o-mini", api_key=openai_api_key,temperature=temp, max_tokens=max_tokens)
       
    else:
        raise ValueError("Invalid model selection")
    response = llm.invoke(query)
    return response.content

def abc():

    pages= {
    " Text generation ": [st.Page("app.py",title="Text to text")],
      "Image to Text": [st.Page("image_text.py",title="image to text")],
       "audio to Text": [st.Page("audio_text.py",title="Audio to text")]
    }
    
    st.navigation(pages)
    
    st.title("LangChain Chatbot")
    st.divider() 
    query = st.text_input("Ask a question:")
    model, temparature, max_tokens = render_sidebar()
   
    if st.button("submit"):

        user = "User"
        Chatbot = "ChatBot"
        output = handle_query(model,query,max_tokens,temparature)
        st.write(f"{user}-->{query}")
        st.write(f"{Chatbot}-->{output}")

abc()

# if __name__ == "__main__":
#     main()