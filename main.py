# -*- coding: utf-8 -*-
"""
Dawson Tocarchick, Nicholas Riggins, Kyle Limbaga

Main.py for Speech to text analysis
"""

import Adafruit_BBIO.GPIO as GPIO

outpin = "P9_12"
GPIO.setup(outpin,GPIO.OUT)
from time import sleep


for i in range(0,5):
    GPIO.output(outpin,GPIO.HIGH)
    print("You Suck")
    sleep(1)
    GPIO.output(outpin,GPIO.LOW)
    print("You rock")
    sleep(1)
GPIO.cleanup()