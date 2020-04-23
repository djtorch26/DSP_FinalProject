# -*- coding: utf-8 -*-
"""
Dawson Tocarchick, Nicholas Riggins, Kyle Limbaga

Speech to text analysis main
"""
#import packages
import os
from time import sleep
from Setup import RecordAudio as record
from Setup import MakeGraphs as mg
from Setup import SendEmail as send


def main():

    #Part 1: Collect audio data from USB microphone
                                &
    #Part 2: Using libraries to determine text output determined
            #by .wav file
    record.get_audio()
    
    #Part 3: Analysis and generation of .wav file
    mg.FFTImage()
    
    #Part 4: Print to console & send Email
    send.emailFile('test.wav')
    send.emailFile('voiceWave.png')
    send.emailFile('FFTwave.png')
    
    
if __name__ == "__main__":
    main()


    