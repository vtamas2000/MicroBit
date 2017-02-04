from microbit import *
import random

currentPosX = [0] #Column
currentPosY = [0] #Row
posHelpX = [0]
posHelpY = [0]
targetPos = [4, 4] #Column, Row


def move(way):

    if way == 0:
        
        for i in range(0, len(currentPosX), 1):
            isNotDone = True
            display.set_pixel(currentPosX[i], currentPosY[i], 9)
            if isNotDone:
                currentPosY[0] = currentPosY[0] - 1
                isNotDone = False
                sleep(1000)
            if i > 0:
                currentPosX[i] = currentPosX[i - 1]
                currentPosY[i] = currentPosY[i - 1]
            if currentPosY[i] == -1:
                currentPosY[i] = 4
        
        
        """display.set_pixel(currentPosX[0], currentPosY[0], 9)
        currentPosY[0] = currentPosY[0] - 1
        sleep(1000)
        if currentPosY[0] == -1:
            currentPosY[0] = 4"""

    if way == 1:
        display.set_pixel(currentPosX[0], currentPosY[0], 9)
        currentPosX[0] = currentPosX[0] + 1
        sleep(1000)
        if currentPosX[0] == 5:
            currentPosX[0] = 0

    if way == 2:
        display.set_pixel(currentPosX[0], currentPosY[0], 9)
        currentPosY[0] = currentPosY[0] + 1
        sleep(1000)
        if currentPosY[0] == 5:
            currentPosY[0] = 0           

    if way == 3:
        display.set_pixel(currentPosX[0], currentPosY[0], 9)
        currentPosX[0] = currentPosX[0] - 1
        sleep(1000)
        if currentPosX[0] == -1:
            currentPosX[0] = 4


def player_move():
    pamacs = 0
    score = 0
    while True:
        right_presses = button_b.get_presses()
        left_presses = button_a.get_presses()
        
        #get_presses resets after returning!!!!!!!!!!!!!!!
        
        pamacs = (pamacs + right_presses - left_presses) % 4 
        move(pamacs)
        display.clear()
        display.set_pixel(targetPos[0], targetPos[1], 4)
        if targetPos[0] == currentPosX[0] and targetPos[1] == currentPosY[0]:
            place_target()
            score = score + 1
            player_growth()


def place_target():
    posX = random.randint(0, 4)
    posY = random.randint(0, 4)
    targetPos[0] = posX
    targetPos[1] = posY
    
def player_growth():
    currentPosX.insert(len(currentPosX), currentPosX[len(currentPosX) - 1])
    currentPosY.insert(len(currentPosY), currentPosY[len(currentPosY) - 1])

def positioning_help():
    
        

while True:
    player_move()