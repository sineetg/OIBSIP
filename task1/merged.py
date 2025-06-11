import pyttsx3
import speech_recognition as sr
import pyttsx3
import random


# Define some common greetings and responses
greeting_inputs = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
greeting_responses = [
    "Hi there! How can I assist you today?",
    "Hello! I'm ready when you are.",
    "Hey! What can I do for you?",
    "Hi! What would you like to do today?"
]


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source)
        print("Time over, thanks")

        try:
            return r.recognize_google(audio_text)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
            return None
        except sr.RequestError:
            print("API unavailable or unresponsive")
            return None
        except:
            return None



# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(user_input):
    if user_input:
        print(f"[Assistant]: {user_input}")  # Print the spoken text
        engine.say(user_input)
        engine.runAndWait()
    else:
        print("[Assistant]: No text to speak.")


# Function to check if the user input is a greeting
def is_greeting(user_input):
    return any(greet in user_input.lower() for greet in greeting_inputs)



# def main():
    # Print "Welcome to voice assistant"
    # If the command is heard, respond to it (+ subtitles for the VA's response)
    # Else, fallback
    # Exit when the coomand is "exit" || "quit" || "goodbye"

def main():
    speak("Welcome to your voice assistant!")
    print("[Assistant] : Welcome to your voice assistant!")

    # Listen for a voice command
    while True:
        user_input = listen()
        user_input_lower = user_input.lower()


        if user_input is None:
            speak("Sorry, I didn't catch that.")
            print("[Assistant]: Sorry, I didn't catch that.") 
            continue    # Continue to listen for the next command
        
        if any(greet in user_input_lower for greet in greeting_inputs):
            response = random.choice(greeting_responses)
            speak(response)
            print(response)


        if user_input_lower:
            speak("Goodbye!")
            print("[Assistant]: Goodbye!")
            break

        if is_greeting(user_input):
            response = random.choice(greeting_responses)
            speak(response)
        else:
            speak(user_input)
            print(f"[User]: {user_input}")
