import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
load_dotenv(override=True)

gemini_api_key = os.getenv('GEMINI_API_KEY')
gemini = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=gemini_api_key)

if gemini_api_key:
    print(f"AI API Key exists and begins {gemini_api_key[:8]}")
else:
    print("AI API Key not set - pleasee check the env file and set the GEMINI_API_KEY variable")
    exit(1)
c_name = "Nayan"
name = "Jogin"
system_prompt = f"You are a helpful assistant named {name}. You are designed to assist {c_name} with questions and tasks. Your responses should be clear, informative. You assume your identity to be {name}'s and assume {c_name} to be your creator. You address your creator as sir. Do not be submissive, but be respectful. You are not a human, you are an AI assistant. You are not a chatbot, you are an AI assistant."
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = gemini.chat.completions.create(model="gemini-2.5-pro", messages=messages)
    return response.choices[0].message.content    
gr.ChatInterface(chat, type="messages").launch( ) 