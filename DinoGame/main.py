from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *
from pynput import keyboard
from threading import Timer
import mss

crouching = False
killBot = False

replaybtn = (950, 415)
dinosaur = (730, 432)
x = 0


def restartGame():
    pyautogui.click(replaybtn)
    pyautogui.press('up')
    print("Play")
    # resetTimer = Timer(30, restartGame)
    # resetTimer.start()


def GrabImage():
    prevTime = time.time()
    offset = 115
    box = (dinosaur[0]+offset, dinosaur[1],
           dinosaur[0]+offset+30, dinosaur[1]+5)
    image = ImageGrab.grab(box)
    # image = mss.mss().grab(
    #     {"top": dinosaur[1], "left": dinosaur[0]+offset, "width": 25, "height": offset+5})
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    newTime = int((time.time() - prevTime) * 1000)
    return a.sum(), newTime


def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.press('space')


def holdDown():
    pyautogui.keyDown('down')


def getColor():
    print(GrabImage()[0])
    return GrabImage()[0]


def onPress(key):
    try:
        k = key.char
    except:
        k = str(key.name)

    global killBot
    if k == "esc":
        killScript()


def killScript():
    global killBot
    killBot = True


listener = keyboard.Listener(on_press=onPress)
listener.start()

time.sleep(2)
restartGame()
Timer(10, killScript).start()

color = getColor()

while True:
    image = GrabImage()

    if (image[0] != color):
        pressSpace()
        crouching = True

    # if (GrabImage() == color and crouching == True):
    #     jumpTimer = Timer(.1, holdDown)
    #     jumpTimer.start()
    #     crouching = False

    if image[0] != color:
        colorChange = True
    else:
        colorChange = False

    x += 1
    print(x, colorChange, image[1])

    if killBot == True:
        break
