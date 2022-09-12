import requests
import pprint
import time
from random import randint

import pygame, sys
import pygame.locals

pygame.init()
BLACK = (0,0,0)
WIDTH = 640
HEIGHT = 512
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)

while True:
    for event in pygame.event.get():
        # if 'key' in event.dict:
        if event.type == 768: # 768 means KeyDown 769 means KeyUp
            if event.key == 97:  # a
                print("a")
            elif event.key == 115: # s
                print("s")
            elif event.key == 100: # d
                print("d")
            elif event.key == 119: # w
                print("w")
            elif event.key == 121: # y
                print("y")
            elif event.key == 104: # h
                print("h")
            elif event.key == 117: # u
                print("u")
            elif event.key == 106: # j
                print("j")
            elif event.key == 105: # i
                print("i")
            elif event.key == 107: # k
                print("k")
            elif event.key == 111: # o
                print("o")
            elif event.key == 108: # l
                print("l")
            elif event.key == 1073741904 : # Arrow
                print("LEFT")
            elif event.key == 1073741905 : # Arrow
                print("DOWN")
            elif event.key == 1073741903 : # Arrow
                print("RIGHT")
            elif event.key == 1073741906 : # Arrow
                print("UP")
            else:
                print(str(event.key) + " " + str(event.unicode))

        if event.type == pygame.locals.QUIT:
             pygame.quit()
             sys.exit()

# # find pygame event keys
# while True:
#     for event in pygame.event.get():
#         # print('{0} pressed'.format(event.dict))
#         if 'key' in event.dict:
#             print('{0}'.format(dir(event)))
#             # print('{0}'.format(str(event.type)))
#             # print('{0} pressed'.format(event.dict))
#             # print(event.dict['key'])
#         if event.type == pygame.locals.QUIT:
#              pygame.quit()
#              sys.exit()



# from pynput.keyboard import Key, Listener

# def on_press(key):
#     print('{0} pressed'.format(key))
#     if key == 'w':
#         # print("w")
#         time.sleep(0.1)
#     if key == 'a':
#         # print("a")
#         time.sleep(0.1)
#     if key == 's':
#         # print("s")
#         time.sleep(0.1)
#     if key == 'd':
#         # print("d")
#         time.sleep(0.1)

# def on_release(key):
#     # print('{0} release'.format(key))

#     if key == Key.esc:
#         # Stop listener

#         return False

# # Collect events until released
# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()