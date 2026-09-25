from groq import Groq
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


def get_api_key():
    # Local development: read from .env
    api_key = os.getenv("GROQ_API_KEY")

    # Streamlit Cloud: read from Streamlit Secrets
    if not api_key:
        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            api_key = None

    return api_key


def generate_response(prompt):

    api_key = get_api_key()

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not configured. "
            "Add GROQ_API_KEY to Streamlit Secrets."
        )

    client = Groq(api_key=api_key)

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_completion_tokens=1500
        )

        return response.choices[0].message.content

    except Exception as e:

        raise RuntimeError(
            f"Groq API Error: {str(e)}"
        )