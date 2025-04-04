import streamlit as st

from pages.APITestGenerator import APITestGenerator
from pages.ChatBot import ChatBot
from pages.RecruiterHelper import RecruiterHelper


class MainApplication:
    def __init__(self, groq_api_key):
        self.recruiter_helper = RecruiterHelper(groq_api_key)
        self.chat_bot = ChatBot(groq_api_key)
        self.api_test_generator = APITestGenerator(groq_api_key)
        self.modules = {
            "📋 Generator Testów API": self.api_test_generator_module,
            "💼 Pomoc dla Rekruterów": self.recruiter_module,
            "💬 Prosty Chatbot": self.chatbot_module
        }

    def run(self):
        st.sidebar.title("🧭 Wybierz moduł aplikacji")
        module_name = st.sidebar.radio("Moduły:", list(self.modules.keys()))

        self.modules[module_name]()

    def api_test_generator_module(self):
        st.title("📋 Generator Testów API")
        api_description = st.text_area("Wprowadź opis API do przetestowania:")

        if st.button("🔧 Generuj Test API"):
            if api_description:
                with st.spinner("Generowanie testu API..."):
                    test_script = self.api_test_generator.generate_api_test(api_description)
                    st.subheader("Wygenerowany Test API")
                    st.markdown(test_script)
            else:
                st.warning("Proszę wpisać opis API.")

    def recruiter_module(self):
        st.title("AI Asystent Rekrutera IT")

        helper = RecruiterHelper(groq_api_key)

        role = st.text_input("Stanowisko")
        technologies = st.text_input("Technologie (opcjonalnie)")

        if st.button("Generuj opis stanowiska"):
            with st.spinner("Generowanie opisu stanowiska..."):
                description = helper.generate_job_description(role, technologies)
                st.markdown(description)

    def chatbot_module(self):
        st.title("💬 Prosty Chatbot")

        user_input = st.text_area("Zapytaj Chatbota:")

        if st.button("🚀 Wyślij"):
            if user_input:
                with st.spinner("Chatbot myśli..."):
                    bot_response = self.chat_bot.chat(user_input)
                    st.markdown(f"**Chatbot:** {bot_response}")
            else:
                st.warning("Wprowadź wiadomość do wysłania.")


# Uruchomienie aplikacji:
if __name__ == "__main__":
    groq_api_key = st.secrets["GROQ_API_KEY"]
    app = MainApplication(groq_api_key)
    app.run()
