#!/bin/bash/python3

# We could probably just use sockets but for ease of use we will use flask to serve, and since the requirements
# require json interaction we will import jsonify as well
from flask import Flask, jsonify, request
import cv2
import time
# from PIL import Image
# from json import JSONEncoder
# import json
# import numpy
import base64
from Raspi_MotorHAT import Raspi_MotorHAT #, Raspi_DCMotor

import time
import atexit

from waitress import serve



# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

def rightHandStep(direction): # 0=Opening,1=Closing
    try:
        if direction == 0:
            # Opens Hand
            myMotor1.run(Raspi_MotorHAT.BACKWARD)
            time.sleep(0.5)
            myMotor1.run(Raspi_MotorHAT.RELEASE)
        if direction == 1:
            # Closes Hand
            myMotor1.run(Raspi_MotorHAT.FORWARD)
            time.sleep(0.5)
            myMotor1.run(Raspi_MotorHAT.RELEASE)
    except KeyboardInterrupt:
        turnOffMotors()
    except Exception as e:
        turnOffMotors()
        print(e)
        
def rightArmStep(direction): # 0=Down,1=Up
    try:
        if direction == 0:
            myMotor2.run(Raspi_MotorHAT.BACKWARD)
            time.sleep(0.1)
            myMotor2.run(Raspi_MotorHAT.RELEASE)
        if direction == 1:
            myMotor2.run(Raspi_MotorHAT.FORWARD)
            time.sleep(0.1)
            myMotor2.run(Raspi_MotorHAT.RELEASE)
    except KeyboardInterrupt:
        turnOffMotors()
    except Exception as e:
        turnOffMotors()
        print(e)
        
def leftHandStep(direction): # 0=Opening,1=Closing
    try:
        if direction == 0:
            myMotor4.run(Raspi_MotorHAT.FORWARD)
            time.sleep(0.5)
            myMotor4.run(Raspi_MotorHAT.RELEASE)
        if direction == 1:
            myMotor4.run(Raspi_MotorHAT.BACKWARD)
            time.sleep(0.5)
            myMotor4.run(Raspi_MotorHAT.RELEASE)
    except KeyboardInterrupt:
        turnOffMotors()
    except Exception as e:
        turnOffMotors()
        print(e)
        
def leftArmStep(direction): # 0=Down,1=Up
    try:
        if direction == 0:
            myMotor3.run(Raspi_MotorHAT.BACKWARD)
            time.sleep(0.1)
            myMotor3.run(Raspi_MotorHAT.RELEASE)
        if direction == 1:
            myMotor3.run(Raspi_MotorHAT.FORWARD)
            time.sleep(0.1)
            myMotor3.run(Raspi_MotorHAT.RELEASE)
    except KeyboardInterrupt:
        turnOffMotors()
    except Exception as e:
        turnOffMotors()
        print(e)

def leftArmUp(steps):
    for each in range(0,steps):
        leftArmStep(1)
    
def leftArmDown(steps):
    for each in range(0,steps):
        leftArmStep(0)
        
def rightArmUp(steps):
    for each in range(0,steps):
        rightArmStep(1)
    
def rightArmDown(steps):
    for each in range(0,steps):
        rightArmStep(0)     

def leftHandOpen(steps):
    for each in range(0,steps):
        leftHandStep(0)

def leftHandClose(steps):
    for each in range(0,steps):
        leftHandStep(1)
        
def rightHandOpen(steps):
    for each in range(0,steps):
        rightHandStep(0)

def rightHandClose(steps):
    for each in range(0,steps):
        rightHandStep(1)



# Instatiate flask server
app = Flask(__name__)

# Set up one endpoint
@app.route('/', methods=['GET'])
def landing():
    ret, image = cam1.read()
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    ret, buffer = cv2.imencode('.jpg',image)
    image64 = base64.b64encode(buffer)
    return jsonify(body=image64), 200

# Final PUT endpoint
@app.route('/', methods=['PUT'])
def string_flip():
    put_input = request.args.get('input')
    # Reverse using slicing
    body_output = put_input[::-1]
    #print("Test")
    # Return reversed string
    return jsonify(body=body_output), 200

## Create App using waitress
# This allows us to build app and deploy using:
# waitress-serve --port=8080 --call mainProduction:create_app
def create_app():
    return app

# Run Code
# if __name__ == '__main__':
#     app.run()

# Run in Waitress mode
if __name__ == "__main__":

    #### create a default object, no changes to I2C address or frequency
    mh = Raspi_MotorHAT(addr=0x6f)
    atexit.register(turnOffMotors)

    #### DC motor test!
    myMotor1 = mh.getMotor(1)
    myMotor2 = mh.getMotor(2)
    myMotor3 = mh.getMotor(3)
    myMotor4 = mh.getMotor(4)

    #### set the speed to start, from 0 (off) to 255 (max speed)
    myMotor1.setSpeed(50)
    myMotor2.setSpeed(100)
    myMotor3.setSpeed(100)
    myMotor4.setSpeed(50)


    # Start Camera
    cam1 = cv2.VideoCapture(2) # Color
    #cam2 = cv2.VideoCapture(0) # Nigh
    time.sleep(2)


    while True:
        if cv2.waitKey(1) == ord('q'):
            break
        serve(app, host="0.0.0.0", port=8080)
    cv2.destroyAllWindows()
    cam1.release()
    
