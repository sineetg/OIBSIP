# TASK 1 

Python Programming with Oasis Infobyte

---

# Voice Assistant

A simple Python-based CLI voice assistant using speech recognition and text-to-speech.  
It can greet, tell the time and date, and perform basic web searches using DuckDuckGo’s Instant Answer API.

---

## Features

- **Voice Recognition:** Listens to your voice commands using the microphone.
- **Text-to-Speech:** Responds to you using speech synthesis.
- **Greetings:** Recognizes greetings and responds accordingly.
- **Time and Date:** Tells the current time and date when asked.
- **Search:** Performs simple web searches and summarizes answers.
- **Exit Commands:** Gracefully exits on commands like "exit", "quit", or "goodbye".

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```
   
2. **Create and activate a virtual environment** (optional but recommended):

  ```
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3. **Install required packages:**

  ```bash
  pip install -r requirements.txt
  ```

---

## Usage
1. Run the assistant:

```bash
python merged.py
```

2. Speak your commands clearly when prompted.

3. Supported commands include:

      - Greetings like “hi”, “hello”, etc.

      - Asking for the time or date (e.g., “What time is it?”)

      - Searching information (e.g., “Search for Python programming”)

      - Exit by saying “exit”, “quit”, or “goodbye”.

---

## Dependencies
  - Python 3.7+
    
  - PyAudio (for microphone access)
  - SpeechRecognition
  - pyttsx3
  - requests

(See full list in requirements.txt)

---

## Notes
   - Ensure your microphone is properly connected and accessible.

   - Internet connection is required for the search feature.

   - The search uses DuckDuckGo’s Instant Answer API and may not cover all queries.

---

## Troubleshooting
   - If speech recognition is not working, check your microphone permissions.

   - PyAudio installation can be tricky on some systems; see PyAudio installation guide if you face issues.

   - For any unexpected errors, restart the assistant.
