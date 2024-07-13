"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai

genai.configure(api_key="AIzaSyAdhHba59C82frkiMmR0U1a5YzfFuYm8DM")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  safety_settings = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    },
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction = "you are a character from gta 5 and now chat with me like that character\n, also do not reply to any questions that are not related to game, instead just say something like you think i am an idiot asking such obvious questions."
)

chat_session = model.start_chat(
  history=[]
)

def ask():
  i = input("You: ")
  # add_his(i,"user")
  return i

def get_response():
  response = chat_session.send_message(ask())
  response = response.text.strip()
  # add_his(response,"model")
  print("character: " + response)
  return response

def add_his(content,role):
  chat_session.history.append({
    "role":role,
    "parts":content
  })
  
while input("int: ")!='0':
  get_response().strip()
  
print(chat_session.history)