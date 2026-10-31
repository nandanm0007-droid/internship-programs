import pyttsx3
engine = pyttsx3.init()
mytext=input("enter some text")
engine.say(mytext)
engine.runAndWait()