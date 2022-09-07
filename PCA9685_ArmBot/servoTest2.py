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

# function main 
def main():
    
    # test1()
    # sleep(5)
    test2()
    sleep(5)
    test3()
    # sleep(5)
    
    # pcaScenario();



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
    srvo_num = 0

    # Angle
    snd_angl = 90
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)


    snd_angl = 110
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)

    snd_angl = 70
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)

    snd_angl = 30
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)


    pcaCleanup()
    time.sleep(0.5)

def test2():
    # Angle
    snd_angl = 90
    for srvo_num in range(nbPCAServo):
        print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
        pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)

    # Angle
    snd_angl = 80
    for srvo_num in range(nbPCAServo):
        print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
        pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)
    pcaCleanup()
    print("Done")


def test3():
    """Declare stiff arm"""

    #Wrist Rotation
    set_servo_angle(0,160)
    
    #Lower Elbow (lower numbers lifts up)
    set_servo_angle(1,160)

    set_servo_angle(2)
    set_servo_angle(3)
    set_servo_angle(4)
    set_servo_angle(5)
    set_servo_angle(6)
    set_servo_angle(7)
    set_servo_angle(8)
    set_servo_angle(9)
    set_servo_angle(10)
    set_servo_angle(11)
    set_servo_angle(12)
    set_servo_angle(13)
    set_servo_angle(14)
    set_servo_angle(15)
    time.sleep(1)
    pcaCleanup()
    print("Done")




if __name__ == '__main__':
    init()
    main()