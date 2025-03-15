import streamlit as st
import sympy as sp
import wolframalpha
import asyncio
from codes.aimodule import ChatBot

API_KEY = st.secrets["general"]["API_KEY"]



client = wolframalpha.Client(API_KEY)
bot = ChatBot('Chandra')

# Streamlit UI layout
st.title("Natural Language Calculator")

st.markdown('')

# Initialize the chat history in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Get user input with chat_input instead of text_input
user_input = st.chat_input("Ask something:")

# When user submits input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": 'user', "content": user_input})
    
    # Display user message
    with st.chat_message('user'):
        st.markdown(user_input)
    
    # Generate bot response
    response = asyncio.run(bot.get_response(user_input))
    
    # Add bot response to chat history
    st.session_state.messages.append({'role': 'assistant', "content": response})
    
    # Display bot response
    with st.chat_message('assistant'):
        st.markdown(response)
    
    # Force a rerun to update the UI
    st.rerun()

# Clear chat history button
if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()
