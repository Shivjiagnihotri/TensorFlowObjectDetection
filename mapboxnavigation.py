import speech_recognition as sr
import pyttsx3
import mapbox

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-6)

# Get a Mapbox Navigation API key from https://www.mapbox.com/pricing/
mapbox_api_key = "pk.eyJ1Ijoic2hpdmppYWduaWhvdHJpIiwiYSI6ImNsaGsyNDdlaTBuZnozZHBiMGEwYXU3cmgifQ.5N7wiq6Sr7yad254of3TVw"

# Create a Mapbox Navigation object
navigation = mapbox.Directions(mapbox_api_key)

# Create a speech recognition object
recognizer = sr.Recognizer()

# Get the user's starting location
print("Where are you starting from?")
engine.say("Where are you starting from?")
engine.runAndWait()
with sr.Microphone() as source:
    audio = recognizer.listen(source)

# Recognize the user's starting location
location = recognizer.recognize_google(audio)

# Get the user's destination
print("Where would you like to go?")
engine.say("Where would you like to go?")
engine.runAndWait()
with sr.Microphone() as source:
    audio = recognizer.listen(source)

# Recognize the user's destination
destination = recognizer.recognize_google(audio)


#this code was added below as a correction
# Replace the location and destination with the correct latitude and longitude coordinates
location = "latitude,longitude"  # Replace with starting location coordinates
destination = "latitude,longitude"  # Replace with destination coordinates

# Get directions from the user's starting location to their destination
response = navigation.directions([location, destination])

# Extract the route from the response
route = response.json()['routes'][0]

# Extract the steps from the route
steps = route['legs'][0]['steps']

# Print and speak the directions to the user
for step in steps:
    print("Turn " + step["maneuver"]["instruction"] + " on " + step["maneuver"]["location"]["street"])
    # Speak the directions to the user using text-to-speech functionality

