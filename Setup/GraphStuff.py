# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:10:07 2020

@author: Dawson
"""
from __future__ import print_function
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
    
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack

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
    
def FFTImage(wav_file):
    fs_rate, signal = wavfile.read(os.path.basename(wav_file))
    print ("Sampling Frequency", fs_rate)
    l_audio = len(signal.shape)
    print ("Channels", l_audio)
    if l_audio == 2:
        signal = signal.sum(axis=1) / 2
    N = signal.shape[0]
    print ("Complete Samplings N", N)
    secs = N / float(fs_rate)
    print ("secs", secs)
    Ts = 1.0/fs_rate # sampling interval in time
    print ("Timestep between samples Ts", Ts)
    t = scipy.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray
    FFT = abs(scipy.fft(signal))
    FFT_side = FFT[range(N//2)] # one side FFT range
    freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
    fft_freqs = np.array(freqs)
    freqs_side = freqs[range(N//2)] # one side frequency range
    fft_freqs_side = np.array(freqs_side)
    plt.subplot(311)
    
    p1 = plt.plot(t, signal, "g") # plotting the signal
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.subplot(312)
    
    p2 = plt.plot(freqs, FFT, "r") # plotting the complete fft spectrum
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count dbl-sided')
    plt.subplot(313)
    
    p3 = plt.plot(freqs_side, abs(FFT_side), "b") # plotting the positive fft spectrum
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count single-sided')
    plt.savefig('FFTwave.png')

#Function Tests
#FFTImage('test.wav')