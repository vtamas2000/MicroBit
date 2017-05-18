from microbit import *
import random

playerOnePoints = 0
playerTwoPoints = 0
#border = Image("00900:00900:00900:00900:00900")

while True:
    oneWins = False
    twoWins = False
    endOfGame = False
    sleepTime = random.randint(2000, 10000)
    sleep(sleepTime)
    display.show(Image.HAPPY)
    while True:
        if button_a.is_pressed():
            playerOnePoints += 1
            oneWins = True
            break
        if button_b.is_pressed():
            playerTwoPoints += 1
            twoWins = True
            break
        if accelerometer.is_gesture("shake"):
            endOfGame = True
            break
    if oneWins:
        display.scroll("1 won")
    if twoWins:
        display.scroll("2 won")
    if endOfGame:
        break

if playerOnePoints > playerTwoPoints:
    display.scroll("1 has won the game")
elif playerTwoPoints > playerOnePoints:
    display.scroll("2 has won the game")
else:
    display.scroll("Döntetlen")
display.scroll(str(playerOnePoints))
display.scroll(str(playerTwoPoints))