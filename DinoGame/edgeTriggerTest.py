import random


class EdgeTrigger(object):
    def __init__(self, callback):
        self.value = None
        self.callback = callback

    def __call__(self, value):
        if value != self.value:
            self.callback(self.value, value)
        self.value = value


def my_callback(oldVal, newVal):
    print("Value changed from {0} to {1}.".format(oldVal, newVal))


detector = EdgeTrigger(my_callback)


for x in range(10):
    number = random.randint(1, 3)
    detector(number)
