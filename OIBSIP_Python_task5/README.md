# TASK 3 

Python Programming with Oasis Infobyte

---

# 💬 Simple Chat Application

A beginner-friendly text-based chat app built in Python using socket programming. This project allows two users to chat with each other in real-time via the command line.

---

## 📌 Features

- Simple client-server chat model
- Real-time 1-to-1 messaging
- Built using Python's built-in `socket` module
- Runs on localhost or across a local network

---

## 🧠 Concepts Used

- Socket Programming
- TCP Connections
- Client-Server Communication

---

## 🛠 Requirements

- Python 3.7+

---

## 🚀 How to Run

### 1. Make sure you have Python installed (version 3.7+).

### 2.Clone this repository or download the folder.

### 3. Open a terminal in the project folder and run the script:

```bash
python server.py
```
This will start the server and wait for a client to connect.

### 4. Start the Client
In another terminal (or another computer on the same network), run:

```bash
python client.py
```
Once connected, users can begin exchanging messages.

---

## 🔐 Notes

- This version supports only one client at a time.

- No encryption or threading — this is kept minimal for learning purposes.

- You can improve it by adding:

   - Multi-client support (using threading)

   - Encryption (using ssl or cryptography)

   - GUI with Tkinter or PyQt

---

 ## 📤 Example Interaction

**Server Terminal:**
```bash
Server started. Waiting for connection on 127.0.0.1:12345...
Connected by ('127.0.0.1', 55678)
You (server): Hello
Client: Hi there!
You (server): How are you?
Client: Doing well, thanks!
```

**Client Terminal:**
```bash
Connected to the server.
Server: Hello
You (client): Hi there!
Server: How are you?
You (client): Doing well, thanks!
```
