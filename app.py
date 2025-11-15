
# app.py
import streamlit as st
from agent import Aryabot

st.set_page_config(page_title="Aryabot", page_icon="🚀")
st.title("Aryabot – Your Cosmic Companion")

bot = Aryabot()

query = st.text_input("Ask Aryabot about space:")
if query:
    response = bot.ask(query)
    st.markdown(response)
