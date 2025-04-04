import streamlit as st
from groq import Groq

class ChatBot:
    def __init__(self, groq_api_key):
        self.client = Groq(api_key=groq_api_key)

    def chat(self, user_input):
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": user_input + ", Odpowiadaj w języku polskim."}],
            model="llama3-8b-8192"
        )
        return response.choices[0].message.content