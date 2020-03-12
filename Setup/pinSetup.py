"""
This module instantiates pins to be used during speech analysis 
"""
import Adafruit_BBIO.ADC as ADC
output = []

def StartSample(pin):
    ADC.setup()
    for i in range(0, 1000):
        output.append(ADC.read_raw(pin))
        print(output[i])