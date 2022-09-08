#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from time import sleep
#Constants
nbPCAServo=16 

# #MG996R Parameters Wide Defaults
# MIN_IMP  =[750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750]
# MAX_IMP  =[2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200]
# MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

#MG996R Parameters Specific Defaults
MIN_IMP  =[780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780]
MAX_IMP  =[2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

# #Parameters
# MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
# MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
# MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]



class ArmBot:

    def __init__(self, medial_rotater=10, medial_extensor=5, medial_flexor=8, distal_flexor=1, distal_rotater=0, distal_grip=4,medial_rotater_angle=10, medial_extensor_angle=5, medial_flexor_angle=8, distal_flexor_angle=1, distal_rotater_angle=0, distal_grip_angle=4):
        """Declare Arm Variables"""
        
        self.motor_record=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.angle_record=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        self.medial_rotater=medial_rotater
        self.motor_record[medial_rotater]="medial_rotater"

        self.medial_extensor=medial_extensor
        self.motor_record[medial_extensor]="medial_extensor"

        self.medial_flexor=medial_flexor
        self.motor_record[medial_flexor]="medial_flexor"

        self.distal_flexor=distal_flexor
        self.motor_record[distal_flexor]="distal_flexor"
        
        self.distal_rotater=distal_rotater
        self.motor_record[distal_rotater]="distal_rotater"
        
        self.distal_grip=distal_grip
        self.motor_record[distal_grip]="distal_grip"

        self.angle_record=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        # self.medial_rotater_angle=medial_rotater_angle
        # self.medial_extensor_angle=medial_extensor_angle
        # self.medial_flexor_angle=medial_flexor_angle
        # self.distal_flexor_angle=distal_flexor_angle
        # self.distal_rotater_angle=distal_rotater_angle
        # self.distal_grip_angle=distal_grip_angle
        
        self.pca = ServoKit(channels=16)
        



    # def __set_resting_angles__(self, medial_rotater_angle=10, medial_extensor_angle=5, medial_flexor_angle=8, distal_flexor_angle=1, distal_rotater_angle=0, distal_grip_angle=4):
    #     self.medial_rotater_angle=medial_rotater_angle
    #     self.medial_extensor_angle=medial_extensor_angle
    #     self.medial_flexor_angle=medial_flexor_angle
    #     self.distal_flexor_angle=distal_flexor_angle
    #     self.distal_rotater_angle=distal_rotater_angle
    #     self.distal_grip_angle=distal_grip_angle
        

    def set_servo_angle(self, srvo_num, snd_angl=None): #disable channel if no angle
        self.pca.servo[srvo_num].angle = snd_angl
        self.angle_record[srvo_num] = snd_angl
        if snd_angl != None:
            print("Send angle {} to Servo {} {}".format(snd_angl,srvo_num,))
        else:
            print("Disabling Channel to Servo {}".format(srvo_num))
        time.sleep(0.01)
        return snd_angl

    def pcaCleanup(self):
        for srvo_num in range(nbPCAServo):
            self.set_servo_angle(srvo_num)
        time.sleep(0.1)
        print("Clean")