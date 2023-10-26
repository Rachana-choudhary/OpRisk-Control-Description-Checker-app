import os
import openai
import toml
import streamlit as st

#secrets = toml.load("secrets.toml")
#openai.api_key = secrets["openai_api_key"]

openai.api_key = st.secrets["openai_api_key"]


def generate_controls(control_description):
    text = f""""Review the description of the operational risk control delimited by triple backticks and provide a detailed feedback on the content in alignment with best practices to document operational risk controls. Your feedback should include the positive aspects of the provided control description, feedback on spelling and grammar mistakes, feedback on gaps in the description and guidance to address these, and revised version of the description which aligns with best practices. {control_description} Please provide the output in where all the headings should be in BOLD and paragraph are in normal font"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=0.6,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response
            
