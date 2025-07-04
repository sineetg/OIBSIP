import pyttsx3

engine = pyttsx3.init()

def speak(text):
    if text:
        print(f"[Assistant]: {text}")  # Print the spoken text
        engine.say(text)
        engine.runAndWait()
    else:
        print("[Assistant]: No text to speak.")
        
# Example usage
speak("Hello, how can I help you today?")
