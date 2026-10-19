import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Set page title
st.title("Chatbot basic (Gemini)")

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Set up session state for Gemini model
if "gemini_model" not in st.session_state:
    st.session_state["gemini_model"] = "gemini-3.8-flash"

# Set up chat messages history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    role = "assistant" if message["role"] == "model" else message["role"]
    with st.chat_message(role):
        st.markdown(message["content"])

# Chat input from user
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Gemini
    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model=st.session_state["gemini_model"],
                contents=prompt,
            )
            
            # قراءة النص مباشرة وعرضه
            bot_reply = response.text
            st.markdown(bot_reply)
            
            # Append model response to session state
            st.session_state.messages.append({"role": "model", "content": bot_reply})
            
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال: {e}")

            