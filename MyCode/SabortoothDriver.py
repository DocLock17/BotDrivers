# Working Sabortooth Code

import RPi.GPIO as GPIO
from time import sleep

ledpin = 18                     # PWM pin connected to LED
timePeriod = 10000
frequency = 50

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)

try:
    pi_pwm = GPIO.PWM(ledpin,frequency)		#create PWM instance with frequency
    # pi_pwm.start(0)				#start PWM of required Duty Cycle 

    pi_pwm.start((1500/timePeriod) * frequency)
    print((1000/timePeriod) * frequency)
    # while True:
    for each in range(3):
        print("Forward UP")
        for duty in range(1500,2010,10):
            pi_pwm.ChangeDutyCycle((duty/timePeriod) * frequency) #provide duty cycle in the range 0-100
            sleep(0.1)
        print(duty)
        print((duty/timePeriod) * frequency)
        sleep(1)
        
        print("Forward Down")
        for duty in range(2000, 1490,-10):
            pi_pwm.ChangeDutyCycle((duty/timePeriod) * frequency)
            sleep(0.1)
        print(duty)
        print((duty/timePeriod) * frequency)
        sleep(5)
        
        print("Backward UP")
        for duty in range(1500, 990,-10):
            pi_pwm.ChangeDutyCycle((duty/timePeriod) * frequency)
            sleep(0.1)
        sleep(1)
        print(duty)
        print((duty/timePeriod) * frequency)
        
        print("Backward Down")
        for duty in range(1000,1510,10):
            pi_pwm.ChangeDutyCycle((duty/timePeriod) * frequency) #provide duty cycle in the range 0-100
            sleep(0.1)
        print(duty)
        print((duty/timePeriod) * frequency)
        sleep(5)

except KeyboardInterrupt:
    print("Keyboard Interrupt")

except Exception as e:
    print(e)
finally:
    print("clean up")
# pi_pwm.cleanup()
GPIO.cleanup()