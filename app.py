import streamlit as st
from agent import ask_agent

st.title("JarVish")

user_input = st.text_area("What do you need help with?")

if st.button("Run"):
    response = ask_agent(user_input)
    st.write(response)
