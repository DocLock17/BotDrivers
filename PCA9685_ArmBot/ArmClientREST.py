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

            elif event.key == 98: # b
                print("b")
                sendKey(event.key)

            elif event.key == 99: # c
                print("c")
                sendKey(event.key)
            
            elif event.key == 100: # d
                print("d")
                sendKey(event.key)

            elif event.key == 101: # e
                print("e")
                sendKey(event.key)

            elif event.key == 102: # f
                print("f")
                sendKey(event.key)

            elif event.key == 103: # g
                print("g")
                sendKey(event.key)  

            elif event.key == 104: # h
                print("h")
                sendKey(event.key)

            elif event.key == 105: # i
                print("i")
                sendKey(event.key)

            elif event.key == 106: # j
                print("j")
                sendKey(event.key)

            elif event.key == 107: # k
                print("k")
                sendKey(event.key)

            elif event.key == 108: # l
                print("l")
                sendKey(event.key)

            elif event.key == 109: # m
                print("m")
                sendKey(event.key)

            elif event.key == 110: # n
                print("n")
                sendKey(event.key)

            elif event.key == 111: # o
                print("o")
                sendKey(event.key)

            elif event.key == 112: # p
                print("p")
                sendKey(event.key)

            elif event.key == 113: # q
                print("q")
                sendKey(event.key)

            elif event.key == 114: # r
                print("r")
                sendKey(event.key)

            elif event.key == 115: # s
                print("s")
                sendKey(event.key)

            elif event.key == 116: # t
                print("t")
                sendKey(event.key)

            elif event.key == 117: # u
                print("u")
                sendKey(event.key)

            elif event.key == 118: # v
                print("v")
                sendKey(event.key)

            elif event.key == 119: # w
                print("w")
                sendKey(event.key)

            elif event.key == 120: # x
                print("x")
                sendKey(event.key)

            elif event.key == 121: # y
                print("y")
                sendKey(event.key)
            
            elif event.key == 122: # z
                print("z")
                sendKey(event.key)

            elif event.key == 48: # 0
                print("0")
                sendKey(event.key)

            elif event.key == 49: # 1
                print("1")
                sendKey(event.key)

            elif event.key == 50: # 2
                print("2")
                sendKey(event.key)

            elif event.key == 51: # 3
                print("3")
                sendKey(event.key)

            elif event.key == 52: # 4
                print("4")
                sendKey(event.key)

            elif event.key == 53: # 5
                print("5")
                sendKey(event.key)

            elif event.key == 54: # 6
                print("6")
                sendKey(event.key)

            elif event.key == 55: # 7
                print("7")
                sendKey(event.key)

            elif event.key == 56: # 8
                print("8")
                sendKey(event.key)

            elif event.key == 57: # 9
                print("9")
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

            elif event.key == 13 : # Return/Enter
                print("Return/Enter")
                sendKey(event.key)

            elif event.key == 32 : # Space
                print("Space")
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

