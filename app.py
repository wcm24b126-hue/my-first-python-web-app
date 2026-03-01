import streamlit as st

st.set_page_config(page_title="Ashan's Web App", page_icon="🚀")

st.title("Welcome to my first Web App! 🇱🇰")
st.write("I built this using Python and the GitHub Student Pack.")

name = st.text_input("What's your name?", "Guest")
major = st.selectbox("What are you studying?", ["CS", "Engineering", "Business", "Other"])

if st.button("Say Hello"):
    st.balloons()
    st.success(f"Hello {name}! It's awesome that you're studying {major}!")
    st.write("Next step: Let's build something even bigger!")
