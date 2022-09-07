#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/

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


# function main 
def main():
    # pcaScenario();
    test1()


# function pcaScenario 
def pcaScenario():
    """Scenario to test servo"""
    for i in range(nbPCAServo):
        for j in range(MIN_ANG[i],MAX_ANG[i],1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG[i],MIN_ANG[i],-1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        pca.servo[i].angle=None #disable channel
        time.sleep(0.5)

def test1():
    """The basics of finding a neutral posture for ArmBot? \
         We will start with sending one servo an angle or two."""

    # Servo number 
    srvo_num = 1

    # Angle
    snd_angl = 70
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    for i in range(1,50):
        pca.servo[srvo_num].angle = snd_angl
        time.sleep(0.01)


    snd_angl = 110
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(0.01)

    snd_angl = 70
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(0.01)

    snd_angl = 110
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(0.01)


if __name__ == '__main__':
    init()
    main()