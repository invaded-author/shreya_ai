import speech_recognition as sr
import pyttsx3
import os
import pyautogui
import time

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Shreya:", text)
    engine.say(text)
    engine.runAndWait()

# Speech recognition
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You:", command)
        return command
    except:
        return ""

# Task executor
def execute_command(command):

    if "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open youtube" in command:
        speak("Opening YouTube")
        os.system("start https://youtube.com")

    elif "shutdown computer" in command:
        speak("Shutting down the computer")
        os.system("shutdown /s /t 5")

    elif "restart computer" in command:
        speak("Restarting computer")
        os.system("shutdown /r /t 5")

    elif "take screenshot" in command:
        speak("Taking screenshot")
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")

    elif "close program" in command:
        speak("Closing active window")
        pyautogui.hotkey("alt","f4")

    elif "sleep" in command:
        speak("Going to sleep mode. Call me when you need me.")

    elif "stop shreya" in command:
        speak("Shutting down assistant. Goodbye.")
        exit()

    else:
        speak("I didn't understand the command")

# Wake word listener
def wake_word_listener():
    speak("Shreya is now running in the background")

    while True:
        text = listen()

        if "shreya" in text:
            speak("Yes, how can I help you?")
            command = listen()
            execute_command(command)

# Start assistant
wake_word_listener()