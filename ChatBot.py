# import openai
# import speech_recognition as sr
# import pyttsx3


#try to implement when on wifi
# from bark import SAMPLE_RATE, generate_audio, preload_models
# from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio

# # download and load all models
# preload_models()

# # generate audio from text
# text_prompt = """
#      Kindly, hold on..., Loading, your, vision AI.
# """
# audio_array = generate_audio(text_prompt)

# # save audio to disk
# write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
  
# # play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)


# # Set up the OpenAI API client with your API key
# openai.api_key = "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"

# # Set up the speech recognition engine
# r = sr.Recognizer()

# # Set up the text-to-speech engine
# engine = pyttsx3.init()

# # Output the greeting message as spoken text
# greeting = "Hello, how can I assist you?"
# print(greeting)
# engine.say(greeting)
# engine.runAndWait()

# # Define a function to take speech input and generate a spoken response
# def talk():
    
#     # Listen for speech input from the user
#     with sr.Microphone() as source:
#         audio = r.listen(source)

#     try:
#         # Use the OpenAI API to generate a response to the user's input
#         prompt = r.recognize_google(audio)
#         response = openai.Completion.create(
#             engine="gpt-3.5-turbo",
#             prompt=prompt,
#             max_tokens=8,
#             temperature=0.5,
#         )
#         answer = response.choices[0].text.strip()

#         # Output the response as spoken text
#         print("You said:", prompt)
#         print("AI says:", answer)
#         engine.say(answer)
#         engine.runAndWait()

#     except sr.UnknownValueError:
#         # Handle speech recognition errors
#         print("Sorry, I didn't understand that.")
#         engine.say("Sorry, I didn't understand that.")
#         engine.runAndWait()
#         talk() #Call the function recursively to get the repeated question
#     except sr.RequestError as e:
#         print("Could not request results from speech recognition service; {0}".format(e))
#         engine.say("Sorry, I'm having trouble connecting to the speech recognition service. Please try again later.")
#         engine.runAndWait()

# # Continuously prompt the user for input until they say "stop"
# while True:
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         prompt = r.recognize_google(audio)
#         if prompt.lower() == "stop":
#             break
#         else:
#             talk()


import openai
import speech_recognition as sr
import psutil  # Import the psutil module to check if the process is running
import pyttsx3
import requests
import subprocess
import time
import os
#used by the navigation
import requests
import json

# Set up the OpenAI API client with your API key
openai.api_key = "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"

# Set up the speech recognition engine
r = sr.Recognizer()

# Set up the text-to-speech engine
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-6)
# engine.say("Kindly, hold on..., Loading, your, vision AI")
# engine.runAndWait()
time.sleep(5)

# Output the greeting message as spoken text
greeting = "Welcome to VISION AI : An innovative platform, developed for the Blind People. How can I assist you?"
print(greeting)
engine.say(greeting)
engine.runAndWait()

# Define a function to check internet connectivity
def check_internet():
    url = "https://www.google.com"
    timeout = 5
    request = requests.get(url, timeout=timeout)
    #print("Internet connection found...")
    return True

# Define a function to take speech input and generate a spoken response
def talk():


    if "how are you" in prompt.lower() or "how are you doing" in prompt.lower() or "hi, how are you" in prompt.lower() or "hello, how are you" in prompt.lower():
        print("You said:", prompt)
        print("AI says: Hello, I am doing well, thank you for asking.")
        engine.say("Hello, I am doing well, thank you for asking.")
        engine.runAndWait()
    elif "hi" in prompt.lower() or "hey" in prompt.lower() or "hello" in prompt.lower():
        print("You said:", prompt)
        print("AI says: Hello!")
        engine.say("Hello!")
        engine.runAndWait()
    elif "thanks" in prompt.lower() or "thank you" in prompt.lower():
        print("You said:", prompt)
        print("AI says: My pleasure!")
        engine.say("My pleasure!")
        engine.runAndWait()
    elif "see" in prompt.lower() or "start" in prompt.lower() or "object detectoin" in prompt.lower() or "vision" in prompt.lower():
        # Start the object detection process
        engine.say("Starting.., Object detection")
        engine.runAndWait()
        object_detection_process = subprocess.Popen(["python", "C:\\Users\\Shivji Agnihotri\\Desktop\\Pieces\\app.py"])
        #UPDATE THE CODE OF OBJECT DETECTION USING TENSORFLOW HERE\DOWNLOAD A BIG SIZE SSD FILE

        #ADD A SEARCH THE DATABASE COMMAND HERE\SEARCH EXCEL

        #ADD A SECTION OF START MY NAVIGATION HERE

    elif "close the object detection" in prompt.lower() or "close" in prompt.lower():
        # Check if the object detection process is running
        if object_detection_process and psutil.pid_exists(object_detection_process.pid):
            # Terminate the object detection process
            engine.say("Turning off object, detection")
            object_detection_process.terminate()
            engine.runAndWait()
        else:
            engine.say("Object detection is not running.")
            engine.runAndWait()
        

    # elif "stop" not in prompt.lower():
    #     if check_internet():
            
    #         # Use the OpenAI API to generate a response to the user's input
    #         response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[{"role": "system", "content":"This is a Blind assistance system.I am a Vision AI. Ask me anything."},{'role': 'user', 'content': prompt}],
    #         max_tokens=8,
    #         n=1,
    #         temperature=0,
    #         top_p=1,
    #         frequency_penalty=0.0,
    #         presence_penalty=0.6,
    #     )
    #         # Get the response text from the API response
    #         answer = response['choices'][0]['message']['content']

    #         # Output the response as spoken text
    #         print("You said:", prompt)
    #         print("AI says:", answer)
    #         engine.say(answer)
    #         engine.runAndWait()
    #     else:
    #         print("Sorry, kindly provide the internet connectivity.\n Or, Please continue with basic commands, such as: \nstart my detection, \nstop my detection, \nstart my navigation.")
    #         engine.say("Sorry, kindly provide the internet connectivity. Or, Please continue with basic commands, such as, start my detection, stop my detection, start my navigation.")
    #         engine.runAndWait()

    elif "navigation" in prompt.lower():
        def get_directions(origin, destination, api_key):
                url = "https://maps.googleapis.com/maps/api/directions/json?"
                parameters = f"origin={origin}&destination={destination}&key={api_key}"
                response = requests.get(url + parameters)
                return json.loads(response.content)

        def get_distance(directions):
            return directions["routes"][0]["legs"][0]["distance"]["text"]

        def get_duration(directions):
            return directions["routes"][0]["legs"][0]["duration"]["text"]

        def navigation_assistant():
            print("Hello! I'm your navigation assistant.")
            origin = input("Please enter your current location: ")
            destination = input("Please enter your destination: ")
            api_key = "YOUR_API_KEY_HERE"
            directions = get_directions(origin, destination, api_key)
            distance = get_distance(directions)
            duration = get_duration(directions)
            print(f"The distance between {origin} and {destination} is {distance} and it will take about {duration}.")
            
        navigation_assistant()

    else:
        # Handle speech recognition errors
        print("Sorry, your voice was not clear.")
        engine.say("Sorry, your voice was not clear.")
        engine.runAndWait()
        #Call the function recursively to get the repeated question
        #talk()

            

    
# Continuously prompt the user for input until they say "stop"
while True:
    
    # Listen for speech input from the user
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            prompt = r.recognize_google(audio, language='en-US')
            if prompt.lower() == "stop":
                answer = "Turning the system off."
                print("AI says:", answer)
                engine.say("Turning the system off. Have a good day!")
                engine.runAndWait()
                break
            else:
                talk()
        except sr.UnknownValueError:
#         # Handle speech recognition errors
            print("Keep talking")
            time.sleep(10)
            engine.say("Keep talking, I am listening to you")
            engine.runAndWait()
            #talk() #Call the function recursively to get the repeated question
        except sr.RequestError as e:
            print("Could not request results from speech recognition service; {0}".format(e))
            engine.say("Sorry, I'm having trouble connecting to the speech recognition service. Please try again later.")
            engine.runAndWait()