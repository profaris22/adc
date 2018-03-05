import os
import time
from time import sleep 
from datetime import datetime
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
adc=Adafruit_ADS1x15.ADS1115()
GAIN=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down = GPIO.PUD_UP)
i=0

while True:
    i=i+1
    open('adc.txt','w').close()
    if i < 10:
        file = open("adc.txt","a")
        b=adc.read_adc(0,gain=GAIN)
        x=(b/65536)*5
        v="%.2f" % x
        print(v)
        file.write(str(i)+","+str(v)+"\n")
        time.sleep(1)
    
    def animate(i):
         graph_data = open('adc.txt','r').read()
         lines = graph_data.split('\n')
         xs = []
         ys = []
         for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(y)
            ax1.clear()
            ax1.plot(xs, ys)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.xlabel('Titik pengukuran')
    plt.ylabel("Tegangan (mv)")
    plt.title('Plotting Tegangan Forward model')
    plt.show()
    
    else:
        i=0
    
  
