import pyttsx3
# rate change code
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
engine.say("Kindly, hold on..., Loading, your, vision AI")

import subprocess
import speech_recognition as sr

#REQUIRED FOR BOT
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch #torch is required by the hugging chat 

# Set up the speech recognition engine
r = sr.Recognizer()

# voice change code ---THIS ONE IS NOT WORKING CORRECTLY
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


#This code is for hug chat
# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

#This code is for hug chat
# Initialize chat history and step
chat_history_ids = None
step = 0

greeting = "Welcome to VISION AI : An innovative platform developed for the Blind People. How can I assist you?"
# Output the initial greeting as spoken text       
print(greeting)
engine.say(greeting)
engine.runAndWait()

# Here's the function to talk
# Define a function to take speech input and generate a spoken response
def talk():
    
    # # Listen for speech input from the user
    # with sr.Microphone() as source:
    #     audio = r.listen(source)

    try:
        # Use the OpenAI API to generate a response to the user's input
        # prompt = r.recognize_google(audio)

        print(f"You said: {prompt}")
        if prompt == "start":
            # Start the object detection process
            engine.say("Starting Object detection")
            object_detection_process = subprocess.Popen(["python", "C:\\Users\\Shivji Agnihotri\\Desktop\\Pieces\\app.py"])
        
        elif prompt == "stop":
            # Terminate the object detection process
            engine.say("Turning off, object, detection")
            engine.runAndWait()
            object_detection_process.terminate()
        
        else: 
            
            #Change here from chatgpt to hugging free chat

            print("User:", prompt)
            
            # Encode the new user input, add the eos_token and return a tensor in Pytorch
            new_user_input_ids = tokenizer.encode(tokenizer.eos_token + propmt, return_tensors='pt')
            
            # Append the new user input tokens to the chat history
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
            
            # Generate a response while limiting the total chat history to 1000 tokens
            chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
            
            # Convert bot's response to speech
            bot_output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
            print("DialoGPT:", bot_output)
            engine.say(bot_output)
            engine.runAndWait()
            
            # Increment step
            step += 1
            
    except sr.UnknownValueError:
        # Handle speech recognition errors
        print("Sorry, I didn't understand that.")
        engine.say("Sorry, I didn't understand that. Can you please repeat your question?")
        engine.runAndWait()
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))
        engine.say("Sorry, I'm having trouble connecting to the speech recognition service. Please try again later.")
        engine.runAndWait()

# Call the talk function to start the conversation
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        prompt = r.recognize_google(audio)
        if prompt.lower() == "stop":
            engine.say("Turning off...")
            engine.runAndWait()
            break
        else:
            # print("try speaking again")
            # engine.say("try speaking again")
            talk()


