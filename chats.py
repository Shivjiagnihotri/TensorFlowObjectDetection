import speech_recognition as sr
import pyttsx3
import requests

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set up connection test URL
url = "http://www.google.com"

# Set up chatbot model and tokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize chat history and step
chat_history_ids = None
step = 0

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

while True:
    # Check internet connection
    try:
        request = requests.get(url, timeout=5)
    except (requests.ConnectionError, requests.Timeout):
        print("No internet connection. Retrying...")
        continue

    # Listen for user input
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Recognize speech input
    try:
        prompt = r.recognize_google(audio)
        print("User:", prompt)
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        continue
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service. Please check your internet connection.")
        continue

    # Encode user input and generate bot response
    new_user_input_ids = tokenizer.encode(tokenizer.eos_token + prompt, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    bot_output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print("DialoGPT:", bot_output)
    
    # Convert bot's response to speech and speak it
    engine.say(bot_output)
    engine.runAndWait()
