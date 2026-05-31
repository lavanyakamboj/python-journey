import pyttsx3
engine = pyttsx3.init()
# engine.say("Hello World!")
engine.say("My current speaking rate is ")
engine.runAndWait()
engine.stop()