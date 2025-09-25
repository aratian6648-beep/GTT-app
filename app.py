# app.py
# --------------------------
# Streamlit Chatbot using Gemini API (google-genai client)
# --------------------------
# Install dependencies first:
#   pip install streamlit google-genai

import streamlit as st
from google import genai

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot with Google Generative AI")

# API Key input (hidden for security)
api_key = "AIzaSyB6ItjhlxI_zGEcuGfya1DukCu4zNtAZpc"

if api_key:
    # Create a client
    client = genai.Client(api_key=api_key)

    # User prompt input
    user_prompt = st.text_area("Your prompt:", "Explain how AI works in a few words")

    if st.button("Generate Response"):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",  # you can change to gemini-1.5-pro etc.
                contents=user_prompt,
            )
            st.subheader("Response:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.warning("⚠️ Please enter your Gemini API key to continue.")