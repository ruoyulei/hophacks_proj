import pyttsx
import time

class speech:
	global engine
	def __init__(self):
		self.engine = pyttsx.init()
		rate = self.engine.getProperty('rate')
		self.engine.setProperty('rate', rate-50)

	def read(self,text):
		self.engine.say(text)
		self.engine.runAndWait()
		# time.sleep(2)
#Sadness sings Adele - Hello "La Voz MMD" | Blind Auditions (eng sub)