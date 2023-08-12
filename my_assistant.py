import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand you.")
            return None
        except sr.RequestError as e:
            print("Sorry, there was an error connecting to Google's servers.")
            return None

def process_command(command):
    if "hello" in command:
        return "Hello there!"
    elif "how are you" in command:
        return "I'm just a computer program, but I'm functioning well!"
    elif "bye" in command:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't know how to respond to that."

if __name__ == "__main__":
    speak("Hello! How can I assist you?")
    while True:
        command = listen()
        if command:
            response = process_command(command.lower())
            speak(response)
