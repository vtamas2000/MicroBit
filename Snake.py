from microbit import *
import random

currentPos = [0, 0] #Column, Row
targetPos = [4, 4] #Column, Row

def move(way):

    if way == 0:
        display.set_pixel(currentPos[0], currentPos[1], 9)
        currentPos[1] = currentPos[1] - 1
        sleep(1000)
        if currentPos[1] == -1:
            currentPos[1] = 4

    if way == 1:
        display.set_pixel(currentPos[0], currentPos[1], 9)
        currentPos[0] = currentPos[0] + 1
        sleep(1000)
        if currentPos[0] == 5:
            currentPos[0] = 0

    if way == 2:
        display.set_pixel(currentPos[0], currentPos[1], 9)
        currentPos[1] = currentPos[1] + 1
        sleep(1000)
        if currentPos[1] == 5:
            currentPos[1] = 0           

    if way == 3:
        display.set_pixel(currentPos[0], currentPos[1], 9)
        currentPos[0] = currentPos[0] - 1
        sleep(1000)
        if currentPos[0] == -1:
            currentPos[0] = 4


def player_move():
    pamacs = 0
    while True:
        right_presses = button_b.get_presses()
        left_presses = button_a.get_presses()
        
        #get_presses resets after returning!!!!!!!!!!!!!!!
        
        pamacs = (pamacs + right_presses - left_presses) % 4 
        move(pamacs)
        display.clear()
        display.set_pixel(targetPos[0], targetPos[1], 4)
        if targetPos[0] == currentPos[0] and targetPos[1] == currentPos[1]:
            place_target()


def place_target():
    posX = random.randint(0, 4)
    posY = random.randint(0, 4)
    targetPos[0] = posX
    targetPos[1] = posY
        

while True:
    player_move()