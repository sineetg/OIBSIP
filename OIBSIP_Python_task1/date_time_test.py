from datetime import datetime
import pyttsx3

print(datetime.now().strftime("%A, %B %d"))
print(datetime.now().strftime("%I:%M %p"))

engine = pyttsx3.init()

def speak():
    current_time = datetime.now().strftime("%I:%M %p")
    current_date = datetime.now().strftime("%A, %B %d")

    text_to_be_spoken = f"The current time is {current_time} and today's date is {current_date}."
    print(text_to_be_spoken)

    engine.say(text_to_be_spoken)
    engine.runAndWait()


speak()