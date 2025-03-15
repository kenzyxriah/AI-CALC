import streamlit as st
import sympy as sp
import wolframalpha
import asyncio
from codes.aimodule import ChatBot, Converter



st.set_page_config(
    page_title="LLM",
    page_icon="📟",
    layout="centered",  # ,Options: 'wide', 'centered'
    initial_sidebar_state= "expanded"
)

API_KEY = st.secrets["general"]["API_KEY"]



client = wolframalpha.Client(API_KEY)
bot = ChatBot('Chandra')



# --- PAGE SETUP ---

# Use Windows + '.' to get useful emojis
about = st.Page(
    page = 'codes/about.py',
    title = 'Main',
    default = True # the first page
)
calc_page = st.Page(
    page = 'codes/calculator.py',
    title = 'Calc',
    icon = '🧭',

)

ai_page = st.Page(
    page = 'codes/wolframbot.py',
    title = 'ChatBot',
    icon = '⛄'
)

converter = st.Page(
    page = 'codes/converter.py',
    title = 'Converter',
    icon = '🧮'
)

# ---- NAVIGATION SETUP ----
pg = st.navigation(
    {
    'Summary' : [about],
    'Projects': [calc_page, ai_page, converter]
    })
pg.run()

st.write("----------------------------")
st.sidebar.text("Built with ❤️ by Yours Truly ")



