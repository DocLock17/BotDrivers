#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from time import sleep
#Constants
nbPCAServo=16 

#need to get the pulse width range of the MG996R
#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

#Objects
pca = ServoKit(channels=16)

# function init 
def init():

    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

def pcaCleanup():
    for srvo_num in range(nbPCAServo):
        set_servo_angle(srvo_num)
    time.sleep(0.1)
    print("Clean")

def set_servo_angle(srvo_num, snd_angl=None): #disable channel if no angle
    pca.servo[srvo_num].angle = snd_angl
    if snd_angl != None:
        print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    else:
        print("Disabling Channel to Servo {}".format(srvo_num))


if __name__ == '__main__':
    init()
    pcaCleanup()
    sleep(5)