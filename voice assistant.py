import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process command and respond
def process_command(command):
    command = command.lower()

    if 'hello' in command:
        response = "Hello! How can I assist you today?"
    elif 'time' in command:
        from datetime import datetime
        now = datetime.now()
        response = f"The current time is {now.strftime('%I:%M %p')}"
    elif 'your name' in command:
        response = "I am your voice assistant."
    elif 'exit' in command:
        response = "Goodbye!"
        speak(response)
        root.destroy()
        return
    else:
        response = "Sorry, I didn't understand that."

    # Display response in GUI
    response_label.config(text="Assistant: " + response)
    # Speak the response
    speak(response)

# Function to capture voice input
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            response_label.config(text="Listening...")
            root.update()
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            command_label.config(text="You said: " + text)
            process_command(text)
        except sr.UnknownValueError:
            response_label.config(text="Sorry, I could not understand.")
            speak("Sorry, I could not understand.")
        except sr.RequestError:
            response_label.config(text="Speech service unavailable.")
            speak("Speech service unavailable.")
        except Exception as e:
            response_label.config(text=f"Error: {str(e)}")
            speak("An error occurred.")

# GUI setup
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("600x500")
root.config(bg="#060F63")

title_label = tk.Label(root, text="Voice Assistant", font=("Arial", 20, "bold"), bg="#1b9b2c")
title_label.pack(pady=10)

command_label = tk.Label(root, text="Click the mic and speak...", font=("Arial", 12), bg="#A7C660")
command_label.pack(pady=10)

mic_button = tk.Button(root, text="🎙️ Speak", font=("Arial", 14), command=listen_command)
mic_button.pack(pady=10)

response_label = tk.Label(root, text="", font=("Arial", 12), bg="#e9dfdf")
response_label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()
