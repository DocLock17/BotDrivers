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
step_setting = 1


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	AB.pcaCleanup()

def process_put(key):
    try:
        if key == 97:  # a
            print("a")
            # AB.soft_step(+step_setting, servo_name="medial_rotater")
            
        elif key == 98: # b
            print("b")
            

        elif key == 99: # c
            print("c")
            
        
        elif key == 100: # d
            print("d")
            # AB.soft_step(-step_setting, servo_name="medial_rotater")
            

        elif key == 101: # e
            print("e")
            # AB.soft_step(-step_setting, servo_name="distal_grip")
            

        elif key == 102: # f
            print("f")
            # AB.soft_step(+step_setting, servo_name="distal_flexor")
            

        elif key == 103: # g
            print("g")
              

        elif key == 104: # h
            print("h")
            

        elif key == 105: # i
            print("i")
            # AB.startup_posture(1)
            

        elif key == 106: # j
            print("j")
            

        elif key == 107: # k
            print("k")
            

        elif key == 108: # l
            print("l")
            

        elif key == 109: # m
            print("m")
            

        elif key == 110: # n
            print("n")
            

        elif key == 111: # o
            print("o")
            

        elif key == 112: # p
            print("p")
            

        elif key == 113: # q
            print("q")
            # AB.soft_step(+step_setting, servo_name="distal_grip")
            

        elif key == 114: # r
            print("r")
            # AB.soft_step(-step_setting, servo_name="distal_flexor")
            

        elif key == 115: # s
            print("s")
            # AB.soft_step(-step_setting, servo_name="medial_flexor")
            

        elif key == 116: # t
            print("t")
            

        elif key == 117: # u
            print("u")
            

        elif key == 118: # v
            print("v")
            

        elif key == 119: # w
            print("w")
            # AB.soft_step(+step_setting, servo_name="medial_flexor")
            

        elif key == 120: # x
            print("x")
            

        elif key == 121: # y
            print("y")
            
        
        elif key == 122: # z
            print("z")
            


        elif key == 48: # 0
            print("0")
            
        elif key == 49: # 1
            print("1")
            # AB.starting_posture(1)

        elif key == 50: # 2
            print("2")
            # AB.reaching_posture(1)
            
        elif key == 51: # 3
            print("3")
            # AB.base_posture(1)
            
        elif key == 52: # 4
            print("4")
            # AB.shutdown_posture(1)
            
        elif key == 53: # 5
            print("5")
            

        elif key == 54: # 6
            print("6")
            

        elif key == 55: # 7
            print("7")
            

        elif key == 56: # 8
            print("8")
            

        elif key == 57: # 9
            print("9")
            
        
        
        elif key == 1073741904 : # Arrow
            print("LEFT")
            # AB.soft_step(+step_setting, servo_name="distal_rotater")
            
        elif key == 1073741905 : # Arrow
            print("DOWN")
            # AB.soft_step(-step_setting, servo_name="medial_extensor")
            
        elif key == 1073741903 : # Arrow
            print("RIGHT")
            # AB.soft_step(-step_setting, servo_name="distal_rotater")
            
        elif key == 1073741906 : # Arrow
            print("UP")
            # AB.soft_step(+step_setting, servo_name="medial_extensor")
            
        elif key == 13 : # Return/Enter
            print("Return/Enter")
            
        elif key == 27 : # ESC
            print("ESC")
            # AB.pcaCleanup()
            
        elif key == 32 : # Space
            print("Space")
            

        else:
            print(str(key) + " ")

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
    # print(put_input)
    process_put(int(put_input))
    # Reverse using slicing
    body_output = put_input
    # print("Test")
    # Return reversed string
    return jsonify(body=body_output), 200

if __name__ == '__main__':
    atexit.register(turnOffMotors)
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')




