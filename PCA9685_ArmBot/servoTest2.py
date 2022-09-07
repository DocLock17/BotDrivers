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
    # test2()
    # sleep(5)
    # test3()
    base_posture(10)
    scene1(10)
    base_posture(10)
    scene2(10)
    base_posture(10)
    pcaCleanup()
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
    snd_angl = 30
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)


    snd_angl = 70
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)

    snd_angl = 90
    print("Send angle {} to Servo {}".format(snd_angl,srvo_num))
    pca.servo[srvo_num].angle = snd_angl
    time.sleep(1)

    snd_angl = 110
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

    # Wrist Rotation (Lower numbers rotate to bots left)
    set_servo_angle(0,125)
    
    # Lower Elbow (lower numbers lifts up) DIstal
    set_servo_angle(1,175)

    # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
    set_servo_angle(2, 25)

    # Base Rotation (Lower numbers move to Bots right)
    set_servo_angle(3, 100)

    # Grip Hand (Lower numbers open grippers)
    set_servo_angle(4, 80)

    # Base Shoulder (lower numbers extend arm away from bot)
    set_servo_angle(5, 140)

    time.sleep(10)
    pcaCleanup()
    print("Done")

def base_posture(hold_time=2):
    """Declare stiff arm"""
    print("Base Posture")

    # Wrist Rotation (Lower numbers rotate to bots left)
    set_servo_angle(0,125)
    
    # Lower Elbow (lower numbers lifts up) DIstal
    set_servo_angle(1,175)

    # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
    set_servo_angle(8, 25)

    # Base Rotation (Lower numbers move to Bots right)
    set_servo_angle(3, 100)

    # Grip Hand (Lower numbers open grippers)
    set_servo_angle(4, 80)

    # Base Shoulder (lower numbers extend arm away from bot)
    set_servo_angle(5, 140)

    time.sleep(hold_time)


def scene1(hold_time=2):
    """Declare stiff arm"""
    print("Scene 1")
    # Wrist Rotation (Lower numbers rotate to bots left)
    set_servo_angle(0,125)
    
    # Lower Elbow (lower numbers lifts up) DIstal
    set_servo_angle(1,170)

    # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
    set_servo_angle(8, 15)

    # Base Rotation (Lower numbers move to Bots right)
    set_servo_angle(3, 100)

    # Grip Hand (Lower numbers open grippers)
    set_servo_angle(4, 80)

    # Base Shoulder (lower numbers extend arm away from bot)
    set_servo_angle(5, 160)

    time.sleep(hold_time)

def scene2(hold_time=2):
    """Declare stiff arm"""
    print("Scene 1")
    # Wrist Rotation (Lower numbers rotate to bots left)
    set_servo_angle(0,125)
    
    # Lower Elbow (lower numbers lifts up) DIstal
    set_servo_angle(1,160)

    # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
    set_servo_angle(8, 55)

    # Base Rotation (Lower numbers move to Bots right)
    set_servo_angle(3, 100)

    # Grip Hand (Lower numbers open grippers)
    set_servo_angle(4, 80)

    # Base Shoulder (lower numbers extend arm away from bot)
    set_servo_angle(5, 120)

    time.sleep(hold_time)


if __name__ == '__main__':
    init()
    main()