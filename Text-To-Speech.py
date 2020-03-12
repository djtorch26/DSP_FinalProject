# -*- coding: utf-8 -*-
"""
Dawson Tocarchick, Nicholas Riggins, Kyle Limbaga

Speech to text analysis main file
"""
#import packages
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
from time import sleep
from Setup import pinSetup

def main():
    """
    Part 1: Collect data from ADC using P9_40 from microphone
    """
    p = pinSetup.StartSample('P9_40')
    print(p)
    """
    Part 2: Analysis and generation of .wav file
    """
    
    """
    Part 3: Using libraries to determine text output determined
            by .wav file
    """
    
    """
    Part 4: Print to console
    """
    
if __name__ == "__main__":
    main()


    