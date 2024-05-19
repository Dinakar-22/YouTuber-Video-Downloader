import os
import streamlit as st
from transformers import pipeline
import torch

st.set_page_config(
    layout='centered',
    page_title='Lue LLM',
    page_icon='🤖'
)

st.header('Lue LLM')

# hf token
os.environ['HF_HUB_TOKEN']="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"

#model name
model_id = "meta-llama/Meta-Llama-3-8B"

model = pipeline("text-generation", model=model_id, trust_remote_code=True)

prompt = st.chat_input("Text Here:")

ans = model(prompt)

st.chat_message("User:").write(prompt)
st.chat_message("Lue:").write(ans)
