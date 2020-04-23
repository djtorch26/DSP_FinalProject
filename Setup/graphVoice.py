# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:10:07 2020

@author: Dawson
"""
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
    
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from scipy.fftpack import fft
from scipy.io import wavfile 

def voiceWavePNG():
    spf = wave.open("test.wav", "r")
    
    # Extract Raw Audio from Wav File
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, "Int16")
    
    
    # If Stereo
    if spf.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)
    
    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(signal)
    plt.savefig('voiceWave.png')
    
def FFTImage():
    fs, data = wavfile.read('test.wav') # load the data
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b) # calculate fourier transform (complex numbers list)
    d = len(c)/2  # you only need half of the fft list (real signal symmetry)
    plt.plot(abs(c[:(d-1)]),'r') 
    plt.savefig('voiceWaveFFT.png')

FFTImage()