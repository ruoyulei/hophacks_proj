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
		time.sleep(1)
		self.engine.runAndWait()