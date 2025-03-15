import streamlit as st
from sympy import sympify, SympifyError


st.title("Scientific Calculator")

# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# Display calculator
expression = st.text_input("Expression", value=st.session_state.display, key="display_input", disabled=False)

# Function to update display
def add_to_display(char):
    st.session_state.display += char
    st.rerun()

def calculate():
    try:
        st.session_state.result = str(sympify(st.session_state.display))
        st.session_state.display = st.session_state.result
    except SympifyError:
        st.session_state.result = "Error"
    st.rerun()

def clear_display():
    st.session_state.display = ""
    st.session_state.result = ""
    st.rerun()

# Create buttons in a grid layout
for i, row in enumerate([
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "(", ")", "CE"]
]):
    cols = st.columns(4)
    for j, btn in enumerate(row):
        if btn == "=":
            if cols[j].button(btn, use_container_width=True):
                calculate()
        elif btn == "C":
            if cols[j].button(btn, use_container_width=True):
                clear_display()
        elif btn == "CE":
            if cols[j].button(btn, use_container_width=True):
                if st.session_state.display:
                    st.session_state.display = st.session_state.display[:-1]
                    st.rerun()
        else:
            if cols[j].button(btn, use_container_width=True):
                add_to_display(btn)

# If user directly inputs a raw expression
if expression != st.session_state.display:
    st.session_state.display = expression
    try:
        st.session_state.result = str(sympify(expression))
    except SympifyError:
        st.session_state.result = "Invalid expression"

# Display result
if st.session_state.result:
    st.success(f"Result: {st.session_state.result}")

  
