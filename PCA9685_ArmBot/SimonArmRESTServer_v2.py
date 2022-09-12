#!/bin/bash/python3

# We could probably just use sockets but for ease of use we will use flask to serve, and since the requirements
# require json interaction we will import jsonify as well
from flask import Flask, jsonify, request
import os

import time

# from json import JSONEncoder
# import json

from ArmBotDriver import ArmBot

import time
import atexit

# from waitress import serve
AB = ArmBot(medial_rotater=10, medial_extensor=5, medial_flexor=8, distal_flexor=1, distal_rotater=0, distal_grip=4)



# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	AB.pcaCleanup()

def process_put(key):
    print("This Key ", key)
    
#  if event.type == 768: # 768 means KeyDown 769 means KeyUp
    if key == 97:  # a
        print("a")
        # sendKey(key)
    elif key == 115: # s
        print("s")
        # sendKey(key)
    elif key == 100: # d
        print("d")
        # sendKey(key)
    elif key == 119: # w
        print("w")
        # sendKey(key)
    elif key == 121: # y
        print("y")
        # sendKey(key)
    elif key == 104: # h
        print("h")
        # sendKey(key)
    elif key == 117: # u
        print("u")
        # sendKey(key)
    elif key == 106: # j
        print("j")
        # sendKey(key)
    elif key == 105: # i
        print("i")
        # sendKey(key)
    elif key == 107: # k
        print("k")
        # sendKey(key)
    elif key == 111: # o
        print("o")
        # sendKey(key)
    elif key == 108: # l
        print("l")
        # sendKey(key)
    elif key == 1073741904 : # Arrow
        print("LEFT")
        # sendKey(key)
    elif key == 1073741905 : # Arrow
        print("DOWN")
        # sendKey(key)
    elif key == 1073741903 : # Arrow
        print("RIGHT")
        # sendKey(key)
    elif key == 1073741906 : # Arrow
        print("UP")
        # sendKey(key)
    else:
        print(str(key) + " ")


def rightHandStep(direction): # 0=Opening,1=Closing
    try:
        print("test")
    except KeyboardInterrupt:
        turnOffMotors()
    except Exception as e:
        turnOffMotors()
        print(e)
        

# Instatiate flask server
app = Flask(__name__)

# Set up one endpoint
@app.route('/', methods=['GET'])
def landing():
    # Return JSON body
    return """Welcome to PalindREST, a simple REST API for reversing a string. Submit a PUT request using the 'input' \
    KEY and a string VALUE of your choice and the reverse string will be returned as the VALUE of the 'body' KEY.""", 200

# Final PUT endpoint
@app.route('/', methods=['PUT'])
def string_flip():
    put_input = request.args.get('input')
    print(put_input)
    process_put(put_input)
    # Reverse using slicing
    body_output = put_input[::-1]
    print("Test")
    # Return reversed string
    return jsonify(body=body_output), 200

if __name__ == '__main__':
    atexit.register(turnOffMotors)
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')


# def process_put(key):
    
# #  if event.type == 768: # 768 means KeyDown 769 means KeyUp
#     if key == 97:  # a
#         print("a")
#         # sendKey(key)
#     elif key == 115: # s
#         print("s")
#         # sendKey(key)
#     elif key == 100: # d
#         print("d")
#         # sendKey(key)
#     elif key == 119: # w
#         print("w")
#         # sendKey(key)
#     elif key == 121: # y
#         print("y")
#         # sendKey(key)
#     elif key == 104: # h
#         print("h")
#         # sendKey(key)
#     elif key == 117: # u
#         print("u")
#         # sendKey(key)
#     elif key == 106: # j
#         print("j")
#         # sendKey(key)
#     elif key == 105: # i
#         print("i")
#         # sendKey(key)
#     elif key == 107: # k
#         print("k")
#         # sendKey(key)
#     elif key == 111: # o
#         print("o")
#         # sendKey(key)
#     elif key == 108: # l
#         print("l")
#         # sendKey(key)
#     elif key == 1073741904 : # Arrow
#         print("LEFT")
#         # sendKey(key)
#     elif key == 1073741905 : # Arrow
#         print("DOWN")
#         # sendKey(key)
#     elif key == 1073741903 : # Arrow
#         print("RIGHT")
#         # sendKey(key)
#     elif key == 1073741906 : # Arrow
#         print("UP")
#         # sendKey(key)
#     else:
#         print(str(key) + " " + str(unicode))




    #  print('q pressed')
    #         #     eventMode = False
    #         if keyboard.is_pressed('esc'):
    #             print('esc pressed')
    #             eventMode = False

    #     # Loop Check For Testing
    #         # print("endless loop", counter)
    #         # counter += 1
    #         # sleep(1)
                
    #         # Trap ASWD
    #         if keyboard.is_pressed('a'):
    #             print('a pressed')
    #             self.soft_step(+step_setting, servo_name="medial_rotater")
    #             # self.soft_step(-step_setting, servo_name="medial_rotater")

    #         if keyboard.is_pressed('s'):
    #             print('s pressed')
    #             # self.soft_step(+step_setting, servo_name="medial_flexor")
    #             self.soft_step(-step_setting, servo_name="medial_flexor")

    #         if keyboard.is_pressed('w'):
    #             print('w pressed')
    #             self.soft_step(+step_setting, servo_name="medial_flexor")
    #             # self.soft_step(-step_setting, servo_name="medial_flexor")

    #         if keyboard.is_pressed('d'):
    #             print('d pressed')
    #             # self.soft_step(+step_setting, servo_name="medial_rotater")
    #             self.soft_step(-step_setting, servo_name="medial_rotater")


            
    #         if keyboard.is_pressed('f'):
    #             print('f pressed')
    #             self.soft_step(+step_setting, servo_name="distal_flexor")
    #             # self.soft_step(-step_setting, servo_name="distal_flexor")

    #         if keyboard.is_pressed('r'):
    #             print('r pressed')
    #             # self.soft_step(+step_setting, servo_name="distal_flexor")
    #             self.soft_step(-step_setting, servo_name="distal_flexor")

    #         if keyboard.is_pressed('q'):
    #             print('q pressed')
    #             self.soft_step(+step_setting, servo_name="distal_grip")
    #             # self.soft_step(-step_setting, servo_name="distal_grip")


    #         if keyboard.is_pressed('e'):
    #             print('e pressed')
    #             # self.soft_step(+step_setting, servo_name="distal_grip")
    #             self.soft_step(-step_setting, servo_name="distal_grip")

            

    #         # Trap LRUP
    #         if keyboard.is_pressed('left'):
    #             print('left pressed')
    #             self.soft_step(+step_setting, servo_name="distal_rotater")
    #             # self.soft_step(-step_setting, servo_name="distal_rotater")

    #         if keyboard.is_pressed('right'):
    #             print('right pressed')
    #             # self.soft_step(+step_setting, servo_name="distal_rotater")
    #             self.soft_step(-step_setting, servo_name="distal_rotater")

    #         if keyboard.is_pressed('up'):
    #             print('up pressed')
    #             self.soft_step(+step_setting, servo_name="medial_extensor")
    #             # self.soft_step(-step_setting, servo_name="medial_extensor")
    #         if keyboard.is_pressed('down'):
    #             print('down pressed')
    #             # self.soft_step(+step_setting, servo_name="medial_extensor")
    #             self.soft_step(-step_setting, servo_name="medial_extensor")


    #         #Trap Numbers for Speed Control
    #         if keyboard.is_pressed('1'):
    #             print('1 pressed')
    #             self.base_posture()
    #         if keyboard.is_pressed('2'):
    #             print('2 pressed')
    #             self.shutdown_posture()
    #         if keyboard.is_pressed('3'):
    #             print('3 pressed')
    #         if keyboard.is_pressed('4'):
    #             print('4 pressed')
    #         if keyboard.is_pressed('5'):
    #             print('5 pressed')
    #         if keyboard.is_pressed('6'):
    #             print('6 pressed')
    #         if keyboard.is_pressed('7'):
    #             print('7 pressed')
    #         if keyboard.is_pressed('8'):
    #             print('8 pressed')            
    #         if keyboard.is_pressed('9'):
    #             print('9 pressed')
    #         if keyboard.is_pressed('0'):
    #             print('0 pressed')

    #         # Trap Special Keys for future uses
    #         if keyboard.is_pressed('space'):
    #             print('space pressed')
    #         if keyboard.is_pressed('enter'):
    #             print('enter pressed')
    #     # key = keyboard.read_event() # Gets the current key code
    #     # print(key) #prints the current key code



