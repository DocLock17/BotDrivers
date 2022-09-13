import requests
# import pprint
# import time
import pygame, sys
import pygame.locals
# from random import randint
# from PIL import Image
# import base64
# import numpy as np
# import cv2
# import io

application_address = 'http://10.0.0.97:8080'

def sendKey(key):
    """ Sends Key Events from pygame to application Server"""
    try:
        query = {'input':key}
        response = requests.put(application_address, params=query)
        print(response.json()['body'])
    except Exception as e:
        print(e)

def getFrame():
    """ Sends Key Events from pygame to application Server"""
    try:
        # response = requests.get(application_address)
        # image = io.BytesIO(base64.b64decode(response.json()['body']))
        image = open("test.jpg", "rb")
        return image
    #Interupt
    # except:
    #     image = previousImage 
    except Exception as e:
        print(e)

pygame.init()
BLACK = (0,0,0)
WIDTH = 480
HEIGHT = 480 #640
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Remote Webcam Viewer')
font = pygame.font.SysFont("Arial",14)
windowSurface.fill(BLACK)

while True:
    for event in pygame.event.get():
        # if 'key' in event.dict:
        if event.type == 768: # 768 means KeyDown 769 means KeyUp
            if event.key == 97:  # a
                print("a")
                sendKey(event.key)
            elif event.key == 115: # s
                print("s")
                sendKey(event.key)
            elif event.key == 100: # d
                print("d")
                sendKey(event.key)
            elif event.key == 119: # w
                print("w")
                sendKey(event.key)
            elif event.key == 121: # y
                print("y")
                sendKey(event.key)
            elif event.key == 104: # h
                print("h")
                sendKey(event.key)
            elif event.key == 117: # u
                print("u")
                sendKey(event.key)
            elif event.key == 106: # j
                print("j")
                sendKey(event.key)
            elif event.key == 105: # i
                print("i")
                sendKey(event.key)
            elif event.key == 107: # k
                print("k")
                sendKey(event.key)
            elif event.key == 111: # o
                print("o")
                sendKey(event.key)
            elif event.key == 108: # l
                print("l")
                sendKey(event.key)
            elif event.key == 1073741904 : # Arrow
                print("LEFT")
                sendKey(event.key)
            elif event.key == 1073741905 : # Arrow
                print("DOWN")
                sendKey(event.key)
            elif event.key == 1073741903 : # Arrow
                print("RIGHT")
                sendKey(event.key)
            elif event.key == 1073741906 : # Arrow
                print("UP")
                sendKey(event.key)
            else:
                print("unstored")
                print(str(event.key) + " " + str(event.unicode))

        if event.type == pygame.locals.QUIT:
             pygame.quit()
             sys.exit()
    # output = pygame.image.load(getFrame())
    # windowSurface.blit(output,(0,0))
    windowSurface.fill(BLACK)
    pygame.display.flip()

