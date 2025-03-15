from codes.aimodule import Converter
import streamlit as st


# Streamlit layout
st.title("Unit Converter")

# State management for input
if "input_value" not in st.session_state:
    st.session_state.input_value = "0"

def update_input(value):
    if st.session_state.input_value == "0":
        st.session_state.input_value = value
    else:
        st.session_state.input_value += value

def clear_input():
    st.session_state.input_value = "0"

def backspace():
    st.session_state.input_value = st.session_state.input_value[:-1] or "0"

# Layout for number buttons
st.text_input("Enter Value:", st.session_state.input_value, disabled=True)

# Button grid with long rectangles
col1, col2, col3 = st.columns(3)

buttons = [
    ("7", "8", "9"),
    ("4", "5", "6"),
    ("1", "2", "3"),
    ("0", ".", "CE"),
    ("⌫",)
]

for row in buttons:
    cols = st.columns([1, 1, 1]) if len(row) == 3 else st.columns([3])
    for i, btn in enumerate(row):
        if cols[i].button(btn, use_container_width=True):
            if btn == "CE":
                clear_input()
            elif btn == "⌫":
                backspace()
            else:
                update_input(btn)

# Dropdown for unit conversion
from_unit = st.selectbox("From Unit:", ["C", "F", "K", "m", "km", "cm", "mm", "in", "kg", "g", "lb", "l", "ml", "m3", "deg", "rad"])
to_unit = st.selectbox("To Unit:", ["C", "F", "K", "m", "km", "cm", "mm", "in", "kg", "g", "lb", "l", "ml", "m3", "deg", "rad"])

# Conversion logic (assuming you have the function `Converter.convert`)
value = float(st.session_state.input_value) if st.session_state.input_value.replace('.', '', 1).isdigit() else 0
result = Converter.convert(value, from_unit, to_unit) or 0

# Display result
st.header(f"Result: {result}")
