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
        if key != 0:
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
# pygame.key.set_repeat(1)
font = pygame.font.SysFont("Arial",14)
windowSurface.fill(BLACK)
this_key = 0

while True:
    for event in pygame.event.get():
        # if 'key' in event.dict:
        if event.type == 768: # 768 means KeyDown 769 means KeyUp

            if event.key == 97:  # a
                print("a")
                this_key = event.key

            elif event.key == 98: # b
                print("b")
                this_key = event.key

            elif event.key == 99: # c
                print("c")
                this_key = event.key
            
            elif event.key == 100: # d
                print("d")
                this_key = event.key

            elif event.key == 101: # e
                print("e")
                this_key = event.key

            elif event.key == 102: # f
                print("f")
                this_key = event.key

            elif event.key == 103: # g
                print("g")
                this_key = event.key  

            elif event.key == 104: # h
                print("h")
                this_key = event.key

            elif event.key == 105: # i
                print("i")
                this_key = event.key

            elif event.key == 106: # j
                print("j")
                this_key = event.key

            elif event.key == 107: # k
                print("k")
                this_key = event.key

            elif event.key == 108: # l
                print("l")
                this_key = event.key

            elif event.key == 109: # m
                print("m")
                this_key = event.key

            elif event.key == 110: # n
                print("n")
                this_key = event.key

            elif event.key == 111: # o
                print("o")
                this_key = event.key

            elif event.key == 112: # p
                print("p")
                this_key = event.key

            elif event.key == 113: # q
                print("q")
                this_key = event.key

            elif event.key == 114: # r
                print("r")
                this_key = event.key

            elif event.key == 115: # s
                print("s")
                this_key = event.key

            elif event.key == 116: # t
                print("t")
                this_key = event.key

            elif event.key == 117: # u
                print("u")
                this_key = event.key

            elif event.key == 118: # v
                print("v")
                this_key = event.key

            elif event.key == 119: # w
                print("w")
                this_key = event.key

            elif event.key == 120: # x
                print("x")
                this_key = event.key

            elif event.key == 121: # y
                print("y")
                this_key = event.key
            
            elif event.key == 122: # z
                print("z")
                this_key = event.key

            elif event.key == 48: # 0
                print("0")
                this_key = event.key

            elif event.key == 49: # 1
                print("1")
                this_key = event.key

            elif event.key == 50: # 2
                print("2")
                this_key = event.key

            elif event.key == 51: # 3
                print("3")
                this_key = event.key

            elif event.key == 52: # 4
                print("4")
                this_key = event.key

            elif event.key == 53: # 5
                print("5")
                this_key = event.key

            elif event.key == 54: # 6
                print("6")
                this_key = event.key

            elif event.key == 55: # 7
                print("7")
                this_key = event.key

            elif event.key == 56: # 8
                print("8")
                this_key = event.key

            elif event.key == 57: # 9
                print("9")
                this_key = event.key
            
            
            elif event.key == 1073741904 : # Arrow
                print("LEFT")
                this_key = event.key
            elif event.key == 1073741905 : # Arrow
                print("DOWN")
                this_key = event.key
            elif event.key == 1073741903 : # Arrow
                print("RIGHT")
                this_key = event.key
            elif event.key == 1073741906 : # Arrow
                print("UP")
                this_key = event.key

            elif event.key == 13 : # Return/Enter
                print("Return/Enter")
                this_key = event.key

            elif event.key == 27 : # ESC
                print("ESC")
                this_key = event.key

            elif event.key == 32 : # Space
                print("Space")
                this_key = event.key

        if event.type == 769: # 768 means KeyDown 769 means KeyUp
            this_key = 0
            
        if event.type == pygame.locals.QUIT:
             pygame.quit()
             sys.exit()
    
    sendKey(this_key)
    # output = pygame.image.load(getFrame())
    # windowSurface.blit(output,(0,0))
    windowSurface.fill(BLACK)
    pygame.display.flip()

