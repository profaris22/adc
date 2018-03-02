import os
import time
from time import sleep 
from datetime import datetime
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

adc=Adafruit_ADS1x15.ADS1115()
GAIN=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down = GPIO.PUD_UP)
i=0
open('adc.txt','w').close()
while i <5:
    file =open('adc.txt','a')
    b=adc.read_adc(0,gain=GAIN)
    x=(b/65536)*5 + 0.12  
    v="%.2f" % x
    print (v)
    i=i+1
    file.write(str(i)+","+str(v)+"\n")
    time.sleep(1)
