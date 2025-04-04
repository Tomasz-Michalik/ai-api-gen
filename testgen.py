import streamlit as st
from groq import Groq

# Ustawienia początkowe aplikacji Streamlit
st.set_page_config(page_title="Generator Testów API", layout="wide")

# Klucz API do Groq (zalecane przechowywanie w zmiennych środowiskowych)
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

# Utworzenie klienta Groq
client = Groq(api_key=GROQ_API_KEY)

# Tytuł aplikacji
st.title("🤖 Generator Testów Automatycznych API")
st.markdown(
    "Automatyczne generowanie testów API w technologiach: **Java + RestAssured**, **JavaScript** oraz **Cypress** przy wsparciu AI.")

# Sidebar nawigacyjny
st.sidebar.title("Nawigacja")
page = st.sidebar.radio("Przejdź do strony:", ["🏠 Strona Główna", "🛠️ Prompty", "📖 Dokumentacja"])

# Strona główna aplikacji
if page == "🏠 Strona Główna":
    st.header("Generowanie testów API")

    tech = st.selectbox("Wybierz technologię testów:", ["Java + RestAssured", "JavaScript", "Cypress"])
    endpoint = st.text_input("Podaj endpoint API:")
    metoda = st.selectbox("Metoda HTTP:", ["GET", "POST", "PUT", "DELETE"])
    opis_testu = st.text_area("Opisz krótko cel testu:")

    if st.button("Generuj test"):
        prompt = f"Napisz test automatyczny API dla endpointu {endpoint} metodą {metoda}, technologia {tech}. Cel testu: {opis_testu}. Zawrzyj komentarze objaśniające."

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1500,
        )

        st.subheader("Wygenerowany test:")
        st.code(response.choices[0].message.content)

# Strona z promptami pomocniczymi
elif page == "🛠️ Prompty":
    st.header("Prompty pomocnicze")

    st.markdown("### Przykładowe prompty do generowania testów:")
    st.code("""
    1. Napisz testy REST API w technologii Java + RestAssured sprawdzające status odpowiedzi oraz poprawność JSON-a.
    2. Przygotuj testy API w JavaScript dla endpointu '/users' metody GET, które walidują status kod 200 i strukturę odpowiedzi.
    3. Stwórz testy integracyjne Cypress do logowania użytkownika, które walidują poprawne logowanie i obsługę błędnych danych.
    """, language="text")

# Dokumentacja projektu
elif page == "📖 Dokumentacja":
    st.header("Dokumentacja Generatora Testów API")
    st.markdown("""
    ### Technologie wykorzystywane w projekcie:
    - **Python, Streamlit** - interfejs użytkownika
    - **Groq API (Llama3-8b)** - model językowy do generowania testów

    ### Sposób użycia:
    - Wybierz technologię, wpisz endpoint API, metodę oraz cel testu.
    - Kliknij "Generuj test", aby uzyskać gotowy kod testu automatycznego.

    ### Dostępne technologie generowania:
    - **Java + RestAssured**
    - **JavaScript (np. Axios, Fetch)**
    - **Cypress**

    ### Wymagane zmienne środowiskowe:
    - `GROQ_API_KEY` - Twój klucz API dostępny na [Groq Console](https://console.groq.com/)
    """)
