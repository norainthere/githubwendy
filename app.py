import os
import streamlit as st
import openai 
from langchain.llms import OpenAI
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Fetch OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set up OpenAI Client
openai.api_key = st.secrets["openai"]["openai_api_key"]
openai_model = 'text-davinci-003'

# Set up OpenAI Playground Trained Model
playground_model = "Wendy"

# Initialize the prompt for generating patch parameters
# Set prompt
prompt = "You are an AI model named \"Wendy\", and when a user gives you descriptive verbal input of a desired sound, you generate a bulleted list of all relevant patch parameter values to be utilized for the software synthesizer \"Serum\". Do you understand?\n\nYes, I understand. I am capable of taking in verbal input from a user and generating a list of relevant patch parameter values for Serum."

# App framework
st.title('🏳️‍⚧️ 🎹Wendy')
# Generate Text
prompt = st.text_input('Describe Your Desired Sound')
if prompt:
    prompt = "generate a " + prompt + " sound for the software synthesizer serum with all relevant parameter values"
    response = openai.Completion.create(
        engine=openai_model,
        prompt=prompt,
        max_tokens=2000
    )
    generated_text = response.choices[0].text
    formatted_text = generated_text.replace("\n", "\n- ")
    st.markdown(f"**Generated Patch Parameters:**\n\n- {formatted_text}")
