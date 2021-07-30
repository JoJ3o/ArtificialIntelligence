# Imports
import mss
from PIL import ImageOps
from PIL import Image
import time
from threading import Timer
import numpy as np

# Functions


def grabImage(coordinates):
    prevTime = time.time()

    image = mss.mss().grab(
        {"top": coordinates[1], "left": coordinates[0], "width": 10, "height": 5})
    imageConvert = Image.frombytes(
        "RGB", image.size, image.bgra, "raw", "BGRX")
    grayImage = ImageOps.grayscale(imageConvert)
    a = np.array(grayImage.getcolors())

    newTime = int((time.time() - prevTime) * 1000)
    return a.sum(), newTime


# Program
offset = 100
dinosaur = (717+offset, 432)

print(grabImage(dinosaur))
