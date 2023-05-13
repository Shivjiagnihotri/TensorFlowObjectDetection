import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1
engine.runAndWait()

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[3].id)
# engine.say("hello")
# engine.runAndWait()