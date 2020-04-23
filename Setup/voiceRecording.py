# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 02:09:36 2020

@author: Dawson
"""

import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with open('test.wav','wb') as f:
        f.write(audio.get_wav_data())
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

get_audio()