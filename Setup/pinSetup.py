"""
This module instantiates pins to be used during speech analysis 
"""
import Adafruit_BBIO.ADC as ADC
output = []


def SampleTime():
    Userinput = input('Enter Record Time in seconds')
    return Userinput
def StartSample(pin):
    t = SampleTime() * 666
    ADC.setup()
    for i in range(0, t): #should be 
        output.append(ADC.read(pin)*1.8)
        print(output[i])
    return output


# 10000/15 samples/sec
# samples * .0015 = seconds recording