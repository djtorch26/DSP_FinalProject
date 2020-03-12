"""
This module instantiates pins to be used during speech analysis 
"""
import Adafruit_BBIO.ADC as ADC
output = []

def StartSample(pin):
    ADC.setup()
    for i in range(0, 8500):
        output.append(ADC.read(pin)*1.8)
        print(output[i])
    return output


# 10000/15 samples/sec
# samples * .0015 = seconds recording