"""
This module instantiates pins to be used during speech analysis 
"""
import Adafruit_BBIO.ADC as ADC
import os

output = []
Devils_Time = 666

def SampleTime():
    Userinput = input('Enter Record Time in seconds: ')
    return Userinput
    # 10000/15 samples/sec
    # samples * .0015 = seconds recording
    
def StartSample(pin):
    t = SampleTime() * Devils_Time
    ADC.setup()
    for i in range(0, t): #should be 
        output.append(ADC.read(pin)*1.8)
        print(output[i])
    return output

def record():
    subprocess.call(arecord )

