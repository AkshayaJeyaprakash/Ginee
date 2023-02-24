import openai
import streamlit as st


def openai_q(query):
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=query,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']

txt = st.text_area('TYPE IN YOUR QUERY HEREEE ....')

st.button("SUBMIT", on_click = st.write(openai_q(txt)))

