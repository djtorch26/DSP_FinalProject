"""
This module instantiates pins to be used during speech analysis 
"""
import Adafruit_BBIO.ADC as ADC
output = []

def StartSample(pin):
    ADC.setup()
    
    for i in range(0,100):
        output[i] = ADC.read_raw(pin)
        return output