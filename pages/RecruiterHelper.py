import streamlit as st
from groq import Groq


class RecruiterHelper:
    def __init__(self, groq_api_key):
        self.client = Groq(api_key=groq_api_key)

    def generate_job_description(self, role, technologies):
        tech_info = f" Uwzględnij następujące technologie: {technologies}." if technologies else ""

        prompt = (
            f"Podaj szczegółowe informacje o roli IT '{role}'. "
            "Uwzględnij obowiązki, najczęściej stosowane technologie, wymagane umiejętności i typowe zadania. "
            f"{tech_info} "
            "Sformatuj odpowiedź w sposób przejrzysty, aby pomóc rekruterom w tworzeniu skutecznych ofert pracy. "
            "zawsze odpowiadaj po polsku."
        )

        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192"
        )

        return response.choices[0].message.content
