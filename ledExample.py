#!/usr/bin/python

# Pi ez connect uses GPIO 18 NOT P18

# Connect Positive LED pin (long) to GPIO 18
# Connect Negative LED pin (short) to 320 ohm resister (Orange Orange Black Black Brown)
# Connect resistor to GROUND

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
try:
    GPIO.setup(18,GPIO.OUT)
    print("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(5)
    print("LED off")
    GPIO.output(18,GPIO.LOW)
except KeyboardInterrupt:
    print("Keyboard Interrupt")
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()