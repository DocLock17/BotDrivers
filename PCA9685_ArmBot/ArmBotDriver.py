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
        self.pca.frequency = 50
        self.nbPCAServo = 16
        
        # self.set_delay = 0.007 # quick but not destroy yourself fast
        # self.set_delay = 0.01 # Smooth
        self.set_delay = 0.014 # Good not exactly gentle or slow though
        # self.set_delay = 0.017 # Slow and gentle but a bit rockety
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
                                          "MAX_ANG":270},
                      "medial_flexor":  {"motor_name": "medial_flexor",
                                         "channel_assingnment":medial_flexor,
                                         "state_angle":0,
                                         "next_angle":0,
                                         "MIN_IMP":780,
                                         "MAX_IMP":2190,
                                         "MIN_ANG":0,
                                         "MAX_ANG":270},
                      "distal_flexor":  {"motor_name": "distal_flexor",
                                         "channel_assingnment":distal_flexor,
                                         "state_angle":0,
                                         "next_angle":0,
                                         "MIN_IMP":780,
                                         "MAX_IMP":2190,
                                         "MIN_ANG":0,
                                         "MAX_ANG":270},
                      "distal_rotater": {"motor_name": "distal_rotater",
                                         "channel_assingnment":distal_rotater,
                                         "state_angle":0,
                                         "next_angle":0,
                                         "MIN_IMP":780,
                                         "MAX_IMP":2190,
                                         "MIN_ANG":0,
                                         "MAX_ANG":270},
                      "distal_grip":    {"motor_name": "distal_grip",
                                         "channel_assingnment":distal_grip,
                                         "state_angle":0,
                                         "next_angle":0,
                                         "MIN_IMP":780,
                                         "MAX_IMP":2190,
                                         "MIN_ANG":0,
                                         "MAX_ANG":270}
                    }

        for i in range(self.nbPCAServo):
            for each in self.state:
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
                        print("Negative")
                        if self.state[each]["next_angle"] < self.state[each]["MIN_ANG"]:
                            self.state[each]["next_angle"] = self.state[each]["MIN_ANG"]
                        self.pca.servo[self.state[each]["channel_assingnment"]].angle = self.state[each]["state_angle"]-step_size
                        self.state[each]["state_angle"] = self.state[each]["state_angle"]-step_size
                    if discrepancy > 0:
                        print("Positive")
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
                    print('NEXT: '+str(self.state[each]["next_angle"]))
                    self.pca.servo[self.state[each]["channel_assingnment"]].angle = self.state[each]["next_angle"]
                    self.state[each]["state_angle"] = self.state[each]["next_angle"]
                    time.sleep(self.set_delay)


    def start_posture(self, hold_time=2):
        """Declare stiff arm"""
        # Base Shoulder (lower numbers extend arm away from bot)
        self.state["medial_extensor"]["next_angle"] = 40 # 5
        # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
        self.state["medial_flexor"]["next_angle"] = 200 # 8
        # Lower Elbow (lower numbers lifts up) DIstal
        self.state["distal_flexor"]["next_angle"] = 135 # 1
        # Base Rotation (Lower numbers move to Bots right)
        self.state["medial_rotater"]["next_angle"] = 135 # 10
        # Wrist Rotation (Lower numbers rotate to bots left)
        self.state["distal_rotater"]["next_angle"] = 135 # 0
        # Grip
        self.state["distal_grip"]["next_angle"] = 150 # 4
        self.rectify_angle("hard")
        time.sleep(hold_time)

    def shutdown_posture(self, hold_time=2):
        """Declare stiff arm"""
        # Base Shoulder (lower numbers extend arm away from bot)
        self.state["medial_extensor"]["next_angle"] = 40 # 5
        # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
        self.state["medial_flexor"]["next_angle"] = 200 # 8
        # Lower Elbow (lower numbers lifts up) DIstal
        self.state["distal_flexor"]["next_angle"] = 135 # 1
        # Base Rotation (Lower numbers move to Bots right)
        self.state["medial_rotater"]["next_angle"] = 135 # 10
        # Wrist Rotation (Lower numbers rotate to bots left)
        self.state["distal_rotater"]["next_angle"] = 135 # 0
        # Grip
        self.state["distal_grip"]["next_angle"] = 150 # 4
        self.rectify_angle()
        time.sleep(hold_time)

    def base_posture(self, hold_time=2):
        """Declare stiff arm"""
        # Base Shoulder (lower numbers extend arm away from bot)
        self.state["medial_extensor"]["next_angle"] = 170 # 5
        # Upper Elbow (Lower numbers lowers arm or Contracts) Medial
        self.state["medial_flexor"]["next_angle"] = 50 # 8
        # Lower Elbow (lower numbers lifts up) DIstal
        self.state["distal_flexor"]["next_angle"] = 270 # 1
        # Base Rotation (Lower numbers move to Bots right)
        self.state["medial_rotater"]["next_angle"] = 135 # 10
        # Wrist Rotation (Lower numbers rotate to bots left)
        self.state["distal_rotater"]["next_angle"] = 135 # 0
        # Grip
        self.state["distal_grip"]["next_angle"] = 150 # 4
        self.rectify_angle()
        time.sleep(hold_time)

    def set_posture(self, hold_time=2, medial_extensor = 86, medial_flexor = 86, distal_flexor = 86, medial_rotater = 86, distal_rotater = 86, distal_grip = 86):
        if medial_extensor != 86:
            self.state["medial_extensor"]["next_angle"] = medial_extensor
        if medial_flexor != 86:
            self.state["medial_flexor"]["next_angle"] = medial_flexor
        if distal_flexor != 86:
            self.state["distal_flexor"]["next_angle"] = distal_flexor
        if medial_rotater != 86:
            self.state["medial_rotater"]["next_angle"] = medial_rotater
        if distal_rotater != 86:
            self.state["distal_rotater"]["next_angle"] = distal_rotater
        if distal_grip != 86:
            self.state["distal_grip"]["next_angle"] = distal_grip
        self.rectify_angle()
        time.sleep(hold_time)

    def soft_step(self, step, servo_number=86, servo_name=""):
        if servo_number != 86:
            for each in self.state:
                if self.state[each]["channel_assingnment"] == servo_number:
                    self.state[each]["next_angle"] = (self.state[each]["state_angle"]+step)
                    print(self.state[each]["state_angle"]+step)
                    self.rectify_angle('hard')
        elif servo_name != "":
            self.state[servo_name]["next_angle"] = (self.state[servo_name]["state_angle"]+step)
            print((self.state[servo_name]["state_angle"]+step))
            self.rectify_angle('hard')

    def step_servo(self, step, servo_number=86, servo_name=""):
        if servo_number != 86:
            for each in self.state:
                if self.state[each]["channel_assingnment"] == servo_number:
                    self.state[each]["next_angle"] = (self.state[each]["state_angle"]+step)
                    print(self.state[each]["state_angle"]+step)
                    self.rectify_angle("hard")
        elif servo_name != "":
            self.state[servo_name]["next_angle"] = (self.state[servo_name]["state_angle"]+step)
            print((self.state[servo_name]["state_angle"]+step))
            self.rectify_angle("hard")

    def flex_servo(self, flex_intensity, hold_time, servo_number=86, servo_name=""):
        if servo_number != 86:
            for each in self.state:
                if self.state[each]["channel_assingnment"] == servo_number:
                    self.state[each]["next_angle"] = (self.state[each]["state_angle"]+flex_intensity)
                    print(self.state[each]["state_angle"]+flex_intensity)
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

    def keyboard_operation(self,step_setting = 3):
        import keyboard
        
        eventMode = True
        counter = 0
        while eventMode == True:
            # Check if Esc or Q has been pressed
            # if keyboard.is_pressed('q'):
            #     print('q pressed')
            #     eventMode = False
            if keyboard.is_pressed('esc'):
                print('esc pressed')
                eventMode = False

        # Loop Check For Testing
            # print("endless loop", counter)
            # counter += 1
            # sleep(1)
                
            # Trap ASWD
            if keyboard.is_pressed('a'):
                print('a pressed')
                self.soft_step(+step_setting, servo_name="medial_rotater")
                # self.soft_step(-step_setting, servo_name="medial_rotater")

            if keyboard.is_pressed('s'):
                print('s pressed')
                # self.soft_step(+step_setting, servo_name="medial_flexor")
                self.soft_step(-step_setting, servo_name="medial_flexor")

            if keyboard.is_pressed('w'):
                print('w pressed')
                self.soft_step(+step_setting, servo_name="medial_flexor")
                # self.soft_step(-step_setting, servo_name="medial_flexor")

            if keyboard.is_pressed('d'):
                print('d pressed')
                # self.soft_step(+step_setting, servo_name="medial_rotater")
                self.soft_step(-step_setting, servo_name="medial_rotater")


            
            if keyboard.is_pressed('f'):
                print('f pressed')
                self.soft_step(+step_setting, servo_name="distal_flexor")
                # self.soft_step(-step_setting, servo_name="distal_flexor")

            if keyboard.is_pressed('r'):
                print('r pressed')
                # self.soft_step(+step_setting, servo_name="distal_flexor")
                self.soft_step(-step_setting, servo_name="distal_flexor")

            if keyboard.is_pressed('q'):
                print('q pressed')
                self.soft_step(+step_setting, servo_name="distal_grip")
                # self.soft_step(-step_setting, servo_name="distal_grip")


            if keyboard.is_pressed('e'):
                print('e pressed')
                # self.soft_step(+step_setting, servo_name="distal_grip")
                self.soft_step(-step_setting, servo_name="distal_grip")

            

            # Trap LRUP
            if keyboard.is_pressed('left'):
                print('left pressed')
                self.soft_step(+step_setting, servo_name="distal_rotater")
                # self.soft_step(-step_setting, servo_name="distal_rotater")

            if keyboard.is_pressed('right'):
                print('right pressed')
                # self.soft_step(+step_setting, servo_name="distal_rotater")
                self.soft_step(-step_setting, servo_name="distal_rotater")

            if keyboard.is_pressed('up'):
                print('up pressed')
                self.soft_step(+step_setting, servo_name="medial_extensor")
                # self.soft_step(-step_setting, servo_name="medial_extensor")
            if keyboard.is_pressed('down'):
                print('down pressed')
                # self.soft_step(+step_setting, servo_name="medial_extensor")
                self.soft_step(-step_setting, servo_name="medial_extensor")


            #Trap Numbers for Speed Control
            if keyboard.is_pressed('1'):
                print('1 pressed')
                self.base_posture()
            if keyboard.is_pressed('2'):
                print('2 pressed')
                self.shutdown_posture()
            if keyboard.is_pressed('3'):
                print('3 pressed')
            if keyboard.is_pressed('4'):
                print('4 pressed')
            if keyboard.is_pressed('5'):
                print('5 pressed')
            if keyboard.is_pressed('6'):
                print('6 pressed')
            if keyboard.is_pressed('7'):
                print('7 pressed')
            if keyboard.is_pressed('8'):
                print('8 pressed')            
            if keyboard.is_pressed('9'):
                print('9 pressed')
            if keyboard.is_pressed('0'):
                print('0 pressed')

            # Trap Special Keys for future uses
            if keyboard.is_pressed('space'):
                print('space pressed')
            if keyboard.is_pressed('enter'):
                print('enter pressed')
        # key = keyboard.read_event() # Gets the current key code
        # print(key) #prints the current key code









if __name__ == '__main__':
    AB = ArmBot(medial_rotater=10, medial_extensor=5, medial_flexor=8, distal_flexor=1, distal_rotater=0, distal_grip=4)

    try:
        AB.start_posture(5)
        # AB.base_posture(5)
        # print("1")
        # AB.flex_servo(20, 1, servo_number=8, servo_name="")
        # print("2")
        # AB.flex_servo(20, 1, servo_number=5)
        # print("3")
        # AB.flex_servo(20, 1, 8)
        # print("4")
        # AB.flex_servo(30, 1, servo_number=86, servo_name="medial_extensor")
        # print("5")
        # AB.flex_servo(20, 1, servo_name="distal_rotater")
        # print("6")
        # AB.flex_servo(20, 1, 86, servo_name="medial_rotater")
        # print("7")
        # AB.flex_servo(40, 1, servo_name="distal_rotater")
        # print("8")
        # AB.flex_servo(40, 1, "medial_rotater")
        # print("Beginning Step Test")
        # time.sleep(2)


        # print("1b")
        # AB.step_servo(-15, servo_number=0, servo_name="")
        # time.sleep(1)
        # print("2b")
        # AB.step_servo(15, servo_number=10)
        # time.sleep(1)
        # print("3b")
        # AB.step_servo(5, 5)
        # time.sleep(1)
        # print("4b")
        # AB.step_servo(-5, servo_number=86, servo_name="medial_extensor")
        # time.sleep(1)
        # print("5b")
        # AB.step_servo(-10, servo_name="medial_flexor")
        # time.sleep(1)
        # print("6b")
        # AB.step_servo(10, 86, servo_name="medial_flexor")
        # time.sleep(1)
        # print("7b")
        # AB.step_servo(-20, servo_name="distal_flexor")
        # time.sleep(1)
        # print("8b")
        # AB.step_servo(20, "distal_flexor")
        # time.sleep(3)
        # AB.set_posture(hold_time=2, distal_flexor = 0)
        # time.sleep(.5)
        # AB.set_posture(hold_time=2, medial_rotater = 20)
        # time.sleep(.5)
        # AB.set_posture(hold_time=2, medial_extensor = 140)
        # time.sleep(.5)
        # AB.set_posture(hold_time=2, medial_extensor = 200)
        # time.sleep(.5)
        # AB.set_posture(hold_time=2, medial_rotater = 230)
        # time.sleep(.5)
        # AB.set_posture(hold_time=2, medial_extensor = 140)
        # time.sleep(.5)
        # AB.set_posture(hold_time=2, medial_extensor = 200)
        # time.sleep(.5)
        print("Entering Manual Control Mode")
        AB.keyboard_operation()
        print("Exiting Manual Control Mode")
        time.sleep(2)

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
