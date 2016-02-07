import pyttsx
import sys

text = sys.argv[1]

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.say(text)
engine.runAndWait()