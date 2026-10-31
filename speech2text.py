import speech_recognition as sr
import pyttsx3
recognizer= sr.Recognizer()
with sr.Microphone()as source:
    print("say something...")
    recognizer.adjust_for_ambient_noise(source)
    audio=recognizer.listen(source)

    try:
        text=recognizer.recognize_google(audio)
        print("you said:",text)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("could not understand the audio")
    except sr.RequestError:
        print("could not request results,check your internet connection")