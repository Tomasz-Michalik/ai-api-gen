import streamlit as st
from groq import Groq


def main():
    # Pobieranie API key z pliku secrets.toml
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

    # Utworzenie klienta Groq
    client = Groq(api_key=GROQ_API_KEY)

    # Pobranie promptu od użytkownika
    user_prompt = st.text_input("Wprowadź prompt:", placeholder="Twój prompt tutaj")

    # Po kliknięciu przycisku wysyłamy żądanie
    if st.button("Wyślij zapytanie"):
        # Wysyłamy żądanie do modelu Groq. Nazwa funkcji send_request jest przykładowa,
        # dostosuj ją do faktycznej implementacji biblioteki.

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.3,
            max_tokens=1500,
        )

        # Wyświetlenie odpowiedzi w konsoli
        print("Odpowiedź:", response.choices[0].message.content)

        # Wyświetlenie odpowiedzi na stronie Streamlit
        st.write("Odpowiedź:", response.choices[0].message.content)

if __name__ == "__main__":
    main()