# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 02:09:36 2020

@author: Dawson
"""

import speech_recognition as sr
from gtts import gTTS
import os
import time

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'test.wav'
    tts.save(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
        
        with open('test.wav','wb') as f:
            f.write(audio.get_wav_data())
		
        said = ""

		try:
		    said = r.recognize_google(audio)
		    print(said)
		except Exception as e:
		    print("Exception: " + str(e))

	return said

