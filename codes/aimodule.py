import os
import streamlit as st
import json
import sympy as sp
import wolframalpha
import asyncio


API_KEY = st.secrets["general"]["API_KEY"]

client = wolframalpha.Client(API_KEY)


class Converter:

    @staticmethod
    def convert(value, from_unit = None, to_unit = None):
        conversions = {
            ("C", "F"): lambda v: (v * 9/5) + 32,
            ("F", "C"): lambda v: (v - 32) * 5/9,
            ("C", "K"): lambda v: v + 273.15,
            ("K", "C"): lambda v: v - 273.15,
            ("m", "km"): lambda v: v / 1000,
            ("km", "m"): lambda v: v * 1000,
            ("cm", "m"): lambda v: v / 100,
            ("m", "cm"): lambda v: v * 100,
            ("mm", "m"): lambda v: v / 1000,
            ("m", "mm"): lambda v: v * 1000,
            ("um", "m"): lambda v: v / 1e6,
            ("m", "um"): lambda v: v * 1e6,
            ("nm", "m"): lambda v: v / 1e9,
            ("m", "nm"): lambda v: v * 1e9,
            ("in", "cm"): lambda v: v * 2.54,
            ("cm", "in"): lambda v: v / 2.54,
            ("kg", "g"): lambda v: v * 1000,
            ("g", "kg"): lambda v: v / 1000,
            ("lb", "kg"): lambda v: v * 0.453592,
            ("kg", "lb"): lambda v: v / 0.453592,
            ("l", "ml"): lambda v: v * 1000,
            ("ml", "l"): lambda v: v / 1000,
            ("m3", "l"): lambda v: v * 1000,
            ("l", "m3"): lambda v: v / 1000,
            ("deg", "rad"): lambda v: v * (sp.pi / 180),
            ("rad", "deg"): lambda v: v * (180 / sp.pi)
        }
        conversion_func = conversions.get((from_unit, to_unit))
        return conversion_func(value) if conversion_func else None
 


class AIHelper:

    @staticmethod
    async def process_input(user_input):
        letter_count = sum(1 for char in user_input if char.isalpha())
        non_letter_count = len(user_input) - letter_count

        if letter_count > non_letter_count:
            return await AIHelper.query_wolfram(user_input)
        else:
            try:
                result = sp.sympify(user_input)
                return f"{result:.2e}" if 'e' in str(result) else str(result)
            except sp.SympifyError:
                wolfram_result = await AIHelper.query_wolfram(user_input)
                return wolfram_result if not wolfram_result.startswith("Wolfram Alpha API Error:") else "Invalid mathematical expression."

    @staticmethod
    async def query_wolfram(query):
        try:
            res = await asyncio.to_thread(client.query, query)

            pods = list(res.pods)
            if pods and len(pods) > 1 and pods[1].subpods:
                return next(pods[1].subpods).plaintext

            return "Wolfram Alpha could not interpret the input."

        except Exception as e:
            return f"Wolfram Alpha API Error:"
        
class ChatBot:
    class ChatBotException(Exception):
        pass

    def __init__(self, name, **kwargs):
        self.name = name


    def get_response(self, input_statement):
        result = AIHelper.process_input(input_statement)
        return result



