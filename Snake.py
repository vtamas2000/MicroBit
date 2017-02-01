from microbit import *
import random

currentPos = [0, 0] #Column, Row
prevPos = [0, 0] #Column, Row

def move(way):

    if way == 0:
        display.set_pixel(currentPos[0], currentPos[1], 9)
        if prevPos[1] != currentPos[1]:
            prevPos[1] = currentPos[1]
        currentPos[1] = currentPos[1] - 1
        sleep(1000)
        if currentPos[1] == -1:
            currentPos[1] = 4
        display.clear()
        #display.set_pixel(prevPos[0], prevPos[1], 0)
        return True


    if way == 1:
        display.set_pixel(currentPos[0], currentPos[1], 9)
        if prevPos[0] != currentPos[0]:
            prevPos[0] = currentPos[0]
        currentPos[0] = currentPos[0] + 1
        sleep(1000)
        if currentPos[0] == 5:
            currentPos[0] = 0
        display.set_pixel(prevPos[0], prevPos[1], 0)
        return True


    if way == 2:
        display.set_pixel(currentPos[0], currentPos[1], 9)
        if prevPos[1] != currentPos[1]:
            prevPos[1] = currentPos[1]
        currentPos[1] = currentPos[1] + 1
        sleep(1000)
        if currentPos[1] == 5:
            currentPos[1] = 0
        display.set_pixel(prevPos[0], prevPos[1], 0)
        return True

    if way == 3:
        display.set_pixel(currentPos[0], currentPos[1], 9)
        if prevPos[0] != currentPos[0]:
            prevPos[0] = currentPos[0]
        currentPos[0] = currentPos[0] - 1
        sleep(1000)
        if currentPos[0] == -1:
            currentPos[0] = 4
        display.set_pixel(prevPos[0], prevPos[1], 0)
        return True
        

while True:
    right_presses = button_b.get_presses()
    left_presses = button_a.get_presses()
    pamacs = (right_presses - left_presses) % 4
    move(pamacs)


