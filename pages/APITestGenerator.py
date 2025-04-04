import streamlit as st
from groq import Groq

class APITestGenerator:
    def __init__(self, groq_api_key):
        self.client = Groq(api_key=groq_api_key)

    def generate_api_test(self, api_description):
        prompt = (
            f"Create a detailed automated API test for the following API description: '{api_description}'. "
            "Use RestAssured with Java or Cypress with JavaScript. Clearly state the test steps, assertions, and test structure."
        )
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192"
        )
        return response.choices[0].message.content
