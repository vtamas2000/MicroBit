from microbit import *
import random
import microbit

playerOneSeaX = []
playerOneSeaY = []
playerTwoSeaX = []
playerTwoSeaY = []
posX = 0
posY = 0
        
def place1x1Ship(playerSeaX, playerSeaY):
    posX = 0
    posY = 0
    display.scroll("1X1 ship")
    sleep(10000)
    posX = button_a.get_presses() 
    posY = button_b.get_presses()
    if posX > 4:
        display.scroll("Invalid position, please try again")
        microbit.reset()
    if posY > 4:
        display.scroll("Invalid position, please try again")
        microbit.reset()
    playerSeaX.append(posX)
    playerSeaY.append(posY)

    
def place2x1Ship(playerSeaX, playerSeaY):
    display.scroll("2X1 ship")
    posX = 0
    posY = 0
    sleep(10000)
    posX = button_a.get_presses() 
    posY = button_b.get_presses()
    if posX > 3:
        display.scroll("Invalid position, please try again")
        microbit.reset()
    if posY > 4:
        display.scroll("Invalid position, please try again")
        microbit.reset()
    playerSeaX.append(posX)
    playerSeaX.append(posX + 1)
    playerSeaY.append(posY)
    playerSeaY.append(posY)
    
def place1x2Ship(playerSeaX, playerSeaY):
    display.scroll("1X2 ship")
    posX = 0
    posY = 0
    sleep(10000)
    posX = button_a.get_presses() 
    posY = button_b.get_presses()
    if posX > 4:
        display.scroll("Invalid position, please try again")
        microbit.reset()
    if posY > 3:
        display.scroll("Invalid position, please try again")
        microbit.reset()
    playerSeaX.append(posX)
    playerSeaX.append(posX)
    playerSeaY.append(posY)
    playerSeaY.append(posY + 1)
    
def playerShipPlacement(playerSeaX, playerSeaY):
    while True:
        place1x1Ship(playerSeaX, playerSeaY)
        place1x1Ship(playerSeaX, playerSeaY)
        place2x1Ship(playerSeaX, playerSeaY)
        place1x2Ship(playerSeaX, playerSeaY) 
        for i in range(0, len(playerSeaX), 1):
            display.set_pixel(playerSeaX[i], playerSeaY[i], 9)
        sleep(2000)
        display.scroll("Confirm?")
        sleep(2000)
        confirm = button_a.get_presses()
        if confirm > 0:
            break

def showPlayerSea(playerSeaX, playerSeaY):
    for i in range(0, len(playerSeaX), 1):
        display.set_pixel(playerSeaX[i], playerSeaY[i], 9)
            
def playerOneFight():
    while True:
        posX = 0
        posY = 0
        hit = False
        display.scroll("1 turns")
        showPlayerSea(playerOneSeaX, playerOneSeaY)
        sleep(3000)
        display.clear()
        display.scroll("Shoot")
        sleep(10000)
        posX = button_a.get_presses()
        posY = button_b.get_presses()
        if posX > 4 or posY > 4:
            display.scroll("Invalid")
            break
        display.set_pixel(posX, posY, 9)
        sleep(2000)
        display.scroll("OK?")
        sleep(2000)
        confirm = button_a.get_presses()
        if confirm > 0:
            display.clear()
            for i in range(0, len(playerTwoSeaX), 1):
                if playerTwoSeaX[i] == posX and playerTwoSeaY[i] == posY:
                    hit = True
                    playerTwoSeaX.remove(posX)
                    playerTwoSeaY.remove(posY)
                    break
            if hit:
                display.show(Image.TARGET)
                sleep(2000)
                break
            else:
                display.show(Image.SAD)
                sleep(2000)
                break
            break

def playerTwoFight():
    while True:
        posX = 0
        posY = 0
        hit = False
        display.scroll("2 turns")
        showPlayerSea(playerTwoSeaX, playerTwoSeaY)
        sleep(3000)
        display.clear()
        display.scroll("Shoot")
        sleep(10000)
        posX = button_a.get_presses()
        posY = button_b.get_presses()
        if posX > 4 or posY > 4:
            display.scroll("Invalid")
            break
        display.set_pixel(posX, posY, 9)
        sleep(2000)
        display.scroll("OK?")
        sleep(2000)
        confirm = button_a.get_presses()
        if confirm > 0:
            display.clear()
            for i in range(0, len(playerOneSeaX), 1):
                if playerOneSeaX[i] == posX and playerOneSeaY[i] == posY:
                    hit = True
                    playerOneSeaX.remove(posX)
                    playerOneSeaY.remove(posY)
                    break
            if hit:
                display.show(Image.TARGET)
                sleep(2000)
                break
            else:
                display.show(Image.SAD)
                sleep(2000)
                break
            break

def checkIfDead(playerSeaX, winner):
    if len(playerSeaX) == 0:
        while True:
            display.scroll("The winner is: Player")
            display.scroll(str(winner))

display.scroll("Player one places ships")
sleep(1000)
playerShipPlacement(playerOneSeaX, playerOneSeaY)
display.scroll("Player two places ships")
sleep(1000)
playerShipPlacement(playerTwoSeaX, playerTwoSeaY)
display.scroll("Fight")
while True:
    playerOneFight()
    checkIfDead(playerTwoSeaX, 1)
    playerTwoFight()
    checkIfDead(playerOneSeaX, 2)