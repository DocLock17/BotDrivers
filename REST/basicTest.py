import speech_recognition as sr

#function to execute voice command

r = sr.Recognizer()

while True:
	with sr.Microphone() as source:
		print 'Say something: '
		#r.adjust_for_ambient_noise(source)

		try:
			audio = r.listen(source,timeout=3) #listening for 3 seconds
		except:
			print "Timeout Exception"

		try:
			text = r.recognize_google(audio)
			print "You said: " , text
			exec_command(text)
		except:
			print "Could not understand"