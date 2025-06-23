# OIBSIP

Python Programming with Oasis Infobyte


# OIBSIP

Python Programming with Oasis Infobyte

---

## Voice Assistant

A simple Python-based voice assistant using speech recognition and text-to-speech.  
It can greet, tell the time and date, and perform basic web searches using DuckDuckGo’s Instant Answer API.

---

## Features

- Recognizes greetings and responds accordingly
- Provides current time and date
- Performs web searches and gives summarized answers
- Uses microphone input and speaks responses aloud
- Graceful handling of unrecognized commands and errors

---

## Requirements

- Python 3.7+
- PyAudio (for microphone access)
- SpeechRecognition
- pyttsx3
- requests

Install dependencies via:

```bash
pip install -r requirements.txt



**Usage**
Run the assistant:

bash
Copy
Edit
python main.py
Speak your commands clearly when prompted.

Supported commands include:

Greetings like “hi”, “hello”, etc.

Asking for the time or date (e.g., “What time is it?”)

Searching information (e.g., “Search for Python programming”)

Exit by saying “exit”, “quit”, or “goodbye”.

**Notes**
Ensure your microphone is properly connected and accessible.

Internet connection is required for the search feature.

The search uses DuckDuckGo’s Instant Answer API and may not cover all queries.

**Troubleshooting**
If speech recognition is not working, check your microphone permissions.

PyAudio installation can be tricky on some systems; see PyAudio installation guide if you face issues.

For any unexpected errors, restart the assistant.
