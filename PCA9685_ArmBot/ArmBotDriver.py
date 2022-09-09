#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
from calendar import c
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from time import sleep

class ArmBot:

    def __init__(self, medial_rotater=10, medial_extensor=5, medial_flexor=8, distal_flexor=1, distal_rotater=0, distal_grip=4):
        """Declare Arm Variables"""
        self.pca = ServoKit(channels=16)
        self.nbPCAServo = 16
        
        # self.set_delay = 0.007 # quick but not destroy yourself fast
        # self.set_delay = 0.01 # Smooth
        # self.set_delay = 0.014 # Good not exactly gentle or slow though
        self.set_delay = 0.018 # Slow and gentle but a bit rockety
        # self.set_delay = 0.02 # TOO ROUGH FOR BOT TO LAST 

        self.state = { "medial_rotater":{"motor_name": "medial_rotater",
                                          "channel_assingnment":medial_rotater,
                                          "state_angle":0,
                                          "next_angle":0,
                                          "MIN_IMP":780,
                                          "MAX_IMP":2190,
                                          "MIN_ANG":0,
                                          "MAX_ANG":270},
                      "medial_extensor":{"motor_name": "medial_extensor",
                                          "channel_assingnment":medial_extensor,
                                          "state_angle":0,
                                          "next_angle":0,
                                          "MIN_IMP":780,
                                          "MAX_IMP":2190,
                                          "MIN_ANG":0,
                                          "MAX_ANG":180},
                      "medial_flexor":  {"motor_name": "medial_flexor",
                                         "channel_assingnment":medial_flexor,
                                         "state_angle":0,
                                         "next_angle":0,
                                         "MIN_IMP":780,
                                         "MAX_IMP":2190,
                                         "MIN_ANG":0,
                                         "MAX_ANG":180},
                      "distal_flexor":  {"motor_name": "distal_flexor",
                                         "channel_assingnment":distal_flexor,
                                         "state_angle":0,
                                         "next_angle":0,
                                         "MIN_IMP":780,
                                         "MAX_IMP":2190,
                                         "MIN_ANG":0,
                                         "MAX_ANG":180},
                      "distal_rotater": {"motor_name": "distal_rotater",
                                         "channel_assingnment":distal_rotater,
                                         "state_angle":0,
                                         "next_angle":0,
                                         "MIN_IMP":780,
                                         "MAX_IMP":2190,
                                         "MIN_ANG":0,
                                         "MAX_ANG":180},
                      "distal_grip":    {"motor_name": "distal_grip",
                                         "channel_assingnment":distal_grip,
                                         "state_angle":0,
                                         "next_angle":0,
                                         "MIN_IMP":780,
                                         "MAX_IMP":2190,
                                         "MIN_ANG":0,
                                         "MAX_ANG":180}
                    }

        for i in range(self.nbPCAServo):
            print(i)
            for each in self.state:
                print(each)
                if self.state[each]["channel_assingnment"] == i:
                    self.pca.servo[i].set_pulse_width_range(self.state[each]["MIN_IMP"], self.state[each]["MAX_IMP"])
                    self.pca.servo[i].actuation_range = self.state[each]["MAX_ANG"]
                    print(str(i)+" "+str(self.pca.servo[i].actuation_range))
                else:
                    self.pca.servo[i].set_pulse_width_range(500, 2500)


    def set_servo_angle(self, srvo_num, snd_angl=None): #disable channel if no angle
        self.pca.servo[srvo_num].angle = snd_angl
        for each in self.state:
            if self.state[each]["channel_assingnment"] == srvo_num:
                self.state[each]["state_angle"] = snd_angl
        if snd_angl != None:
            print("Send angle {} to Servo {} {}".format(snd_angl,srvo_num,))
        else:
            print("Disabling Channel to Servo {}".format(srvo_num))
        time.sleep(self.set_delay)
        return snd_angl


    def pcaCleanup(self):
        for srvo_num in range(self.nbPCAServo):
            self.set_servo_angle(srvo_num)
        time.sleep(self.set_delay)
        # print("Clean")


    def rectify_angle(self, mode='soft', step_size=1): #disable channel if no angle
        if mode == 'soft':
            discrepancy_list = [x for x in self.state if self.state[x]["state_angle"] != self.state[x]["next_angle"]]
            while len(discrepancy_list):
                for each in discrepancy_list:
                    discrepancy = self.state[each]["next_angle"]-self.state[each]["state_angle"]
                    if abs(discrepancy) < step_size:
                        step_size = abs(discrepancy)
                    if discrepancy < 0:
                        # print("Negative")
                        if self.state[each]["next_angle"] < self.state[each]["MIN_ANG"]:
                            self.state[each]["next_angle"] = self.state[each]["MIN_ANG"]
                        self.pca.servo[self.state[each]["channel_assingnment"]].angle = self.state[each]["state_angle"]-step_size
                        self.state[each]["state_angle"] = self.state[each]["state_angle"]-step_size
                    if discrepancy > 0:
                        # print("Positive")
                        if self.state[each]["next_angle"] > self.state[each]["MAX_ANG"]:
                            self.state[each]["next_angle"] = self.state[each]["MAX_ANG"]
                        self.pca.servo[self.state[each]["channel_assingnment"]].angle = self.state[each]["state_angle"]+step_size
                        self.state[each]["state_angle"] = self.state[each]["state_angle"]+step_size
                discrepancy_list = [x for x in self.state if self.state[x]["state_angle"] != self.state[x]["next_angle"]]
                time.sleep(self.set_delay) # Really fast

        if mode == 'hard':
            for each in self.state:
                 if self.state[each]["state_angle"] != self.state[each]["next_angle"]:
                    if self.state[each]["next_angle"] > self.state[each]["MAX_ANG"]:
                        self.state[each]["next_angle"] = self.state[each]["MAX_ANG"]
                    if self.state[each]["next_angle"] < self.state[each]["MIN_ANG"]:
                        self.state[each]["next_angle"] = self.state[each]["MIN_ANG"]
                    self.pca.servo[self.state[each]["channel_assingnment"]].angle = self.state[each]["next_angle"]
                    self.state[each]["state_angle"] = self.state[each]["next_angle"]
                    time.sleep(self.set_delay)


    def start_posture(self, hold_time=2):
        """Declare stiff arm"""
        # Base Shoulder (lower numbers extend arm away from bot)
        self.state["medial_extensor"]["next_angle"] = 2 # 5
        # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
        self.state["medial_flexor"]["next_angle"] = 144 # 8
        # Lower Elbow (lower numbers lifts up) DIstal
        self.state["distal_flexor"]["next_angle"] = 114 # 1
        # Base Rotation (Lower numbers move to Bots right)
        self.state["medial_rotater"]["next_angle"] = 110 # 10
        # Wrist Rotation (Lower numbers rotate to bots left)
        self.state["distal_rotater"]["next_angle"] = 124 # 0
        # Grip
        self.state["distal_grip"]["next_angle"] = 80 # 4
        self.rectify_angle("hard")
        time.sleep(hold_time)

    def shutdown_posture(self, hold_time=2):
        """Declare stiff arm"""
        # Base Shoulder (lower numbers extend arm away from bot)
        self.state["medial_extensor"]["next_angle"] = 2 # 5
        # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
        self.state["medial_flexor"]["next_angle"] = 144 # 8
        # Lower Elbow (lower numbers lifts up) DIstal
        self.state["distal_flexor"]["next_angle"] = 114 # 1
        # Base Rotation (Lower numbers move to Bots right)
        self.state["medial_rotater"]["next_angle"] = 110 # 10
        # Wrist Rotation (Lower numbers rotate to bots left)
        self.state["distal_rotater"]["next_angle"] = 124 # 0
        # Grip
        self.state["distal_grip"]["next_angle"] = 80 # 4
        self.rectify_angle()
        time.sleep(hold_time)

    def base_posture(self, hold_time=2):
        """Declare stiff arm"""
        # Base Shoulder (lower numbers extend arm away from bot)
        self.state["medial_extensor"]["next_angle"] = 140 # 5
        # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
        self.state["medial_flexor"]["next_angle"] = 36 # 8
        # Lower Elbow (lower numbers lifts up) DIstal
        self.state["distal_flexor"]["next_angle"] = 180 # 1
        # Base Rotation (Lower numbers move to Bots right)
        self.state["medial_rotater"]["next_angle"] = 110 # 10
        # Wrist Rotation (Lower numbers rotate to bots left)
        self.state["distal_rotater"]["next_angle"] = 124 # 0
        # Grip
        self.state["distal_grip"]["next_angle"] = 80 # 4
        self.rectify_angle()
        time.sleep(hold_time)


    def flex_servo(self, flex_intensity, hold_time, servo_number=86, servo_name=""):
        if servo_number != 86:
            for each in self.state:
                if self.state[each]["channel_assingnment"] == servo_number:
                    print(self.state[each]["state_angle"]+flex_intensity)
                    self.state[each]["next_angle"] = (self.state[each]["state_angle"]+flex_intensity)
                    self.rectify_angle()
                    time.sleep(hold_time)

                    self.state[each]["next_angle"] = (self.state[each]["state_angle"]-flex_intensity)
                    print(self.state[each]["state_angle"]-flex_intensity)
                    self.rectify_angle()
                    time.sleep(hold_time)
                    
                    self.state[each]["next_angle"] = (self.state[each]["state_angle"]-flex_intensity)
                    print(self.state[each]["state_angle"]-flex_intensity)
                    self.rectify_angle()
                    time.sleep(hold_time)

                    self.state[each]["next_angle"] = (self.state[each]["state_angle"]+flex_intensity)
                    print(self.state[each]["state_angle"]+flex_intensity)
                    self.rectify_angle()
                    time.sleep(hold_time)

        elif servo_name != "":
            self.state[servo_name]["next_angle"] = (self.state[servo_name]["state_angle"]+flex_intensity)
            print((self.state[servo_name]["state_angle"]+flex_intensity))
            self.rectify_angle()
            time.sleep(hold_time)

            self.state[servo_name]["next_angle"] = (self.state[servo_name]["state_angle"]-flex_intensity)
            print((self.state[servo_name]["state_angle"]-flex_intensity))
            self.rectify_angle()
            time.sleep(hold_time)

            self.state[servo_name]["next_angle"] = (self.state[servo_name]["state_angle"]-flex_intensity)
            print((self.state[servo_name]["state_angle"]-flex_intensity))
            self.rectify_angle()
            time.sleep(hold_time)

            self.state[servo_name]["next_angle"] = (self.state[servo_name]["state_angle"]+flex_intensity)
            print((self.state[servo_name]["state_angle"]+flex_intensity))
            self.rectify_angle()
            time.sleep(hold_time)

        else:
            raise Exception("Unidentified Servo Error")

if __name__ == '__main__':
    AB = ArmBot(medial_rotater=10, medial_extensor=5, medial_flexor=8, distal_flexor=1, distal_rotater=0, distal_grip=4)

    try:
        AB.start_posture(5)
        AB.base_posture(5)
        print("1")
        AB.flex_servo(30, 1, servo_number=10, servo_name="")
        print("2")
        AB.flex_servo(40, 1, servo_number=10)
        print("3")
        AB.flex_servo(50, 1, 10)
        print("4")
        AB.flex_servo(60, 1, servo_number=86, servo_name="medial_rotater")
        print("5")
        AB.flex_servo(70, 1, servo_name="medial_rotater")
        print("6")
        AB.flex_servo(80, 1, 86, servo_name="medial_rotater")
        print("7")
        AB.flex_servo(90, 1, servo_name="medial_rotater")
        print("8")
        AB.flex_servo(30, 1, "medial_rotater")
        print("Shutting down . . .")
        AB.shutdown_posture()
        print("Done")
    except Exception as e:
        print(e)
    finally:
        AB.pcaCleanup()
        print("Clean")





# Notes
# # # MG996R Parameters Specific Defaults
# self.MIN_IMP  = [780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780, 780]
# self.MAX_IMP  = [2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190, 2190]
# self.MIN_ANG  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# self.MAX_ANG  = [180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

# # MG996R Parameters Wide Defaults
# self.MIN_IMP  =[750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750]
# self.MAX_IMP  =[2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200, 2200]
# self.MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# self.MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

# # Base Parameters
# self.MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
# self.MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
# self.MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# self.MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]
