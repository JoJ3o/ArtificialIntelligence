# Imports
from typing import NewType
from PIL import ImageGrab
from PIL import ImageOps
from PIL import Image
import pyautogui
import time
from numpy import *
from pynput import keyboard
from threading import Timer
from threading import Thread
import mss

# Classes


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        # print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


# Functions
crouching = False
killBot = False


def restartGame():
    replaybtn = (950, 415)
    pyautogui.click(replaybtn)
    pyautogui.press('up')
    print("Play")
    # resetTimer = Timer(30, restartGame)
    # resetTimer.start()


def grabImagePIL(coordinates):
    prevTime = time.time()
    box = (coordinates[0], coordinates[1],
           coordinates[0]+10, coordinates[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    newTime = int((time.time() - prevTime) * 1000)
    return a.sum(), newTime


def grabImageMss(coordinates):
    prevTime = time.time()
    image = mss.mss().grab(
        {"top": coordinates[1], "left": coordinates[0], "width": 10, "height": 5})
    imageConvert = Image.frombytes(
        "RGB", image.size, image.bgra, "raw", "BGRX")
    grayImage = ImageOps.grayscale(imageConvert)
    a = array(grayImage.getcolors())
    newTime = int((time.time() - prevTime) * 1000)
    return a.sum(), newTime


def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.press('space')


def holdDown():
    pyautogui.keyDown('down')


def getColor(coordinates):
    print(grabImageMss(coordinates)[0])
    return grabImageMss(coordinates)[0]


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


def getImage():
    image = grabImageMss(dinosaur)
    print(image[1])
    return image


def increaseX(number):
    number += 1
    return number


# Program
listener = keyboard.Listener(on_press=onPress)
listener.start()

time.sleep(2)
restartGame()
Timer(10, killScript).start()

dinosaur = (717+100, 432)
color = getColor(dinosaur)
x = 0

while True:
    imageThread = ThreadWithReturnValue(target=getImage)
    imageThread.start()
    # imageInfo = imageThread.join()

    # if (image[0] != color):
    #     pressSpace()
    #     crouching = True

    # if (GrabImage() == color and crouching == True):
    #     jumpTimer = Timer(.1, holdDown)
    #     jumpTimer.start()
    #     crouching = False

    # if image[0] != color:
    #     colorChange = True
    # else:
    #     colorChange = False

    newX = increaseX(x)
    x = newX

    print(x)

    if killBot == True:
        break
