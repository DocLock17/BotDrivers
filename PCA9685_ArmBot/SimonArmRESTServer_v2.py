#!/bin/bash/python3

# We could probably just use sockets but for ease of use we will use flask to serve, and since the requirements
# require json interaction we will import jsonify as well
from flask import Flask, jsonify, request

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
    # Reverse using slicing
    body_output = put_input[::-1]
    print("Test")
    # Return reversed string
    return jsonify(body=body_output), 200

if __name__ == '__main__':
    atexit.register(turnOffMotors)
    app.run()
