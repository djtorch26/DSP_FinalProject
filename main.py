# -*- coding: utf-8 -*-
"""
Dawson Tocarchick, Nicholas Riggins, Kyle Limbaga

Main.py for Speech to text analysis
"""
#import packages
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
from time import sleep
import adc_setup as adc

#setup and pin Instantiations
outpin = "P9_12"
GPIO.setup(outpin,GPIO.OUT)
adc.setup_adc()

value = ADC.read('AIN1')
voltage = value * 1.8
loop = True

while loop:
    print(' Value = %(val) \n Voltage = %(volt)' %{'val': value, 'volt': voltage})
    sleep(.5)
    