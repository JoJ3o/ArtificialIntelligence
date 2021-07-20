import time
from threading import Thread, Timer


def test(ab):
    print(ab[0])
    time.sleep(1)
    ab[0] += 1
    if running[0]:
        Thread(target=test, args=(a,)).start()


def kill(running):
    running[0] = False


running = [True]
Timer(5, kill, args=(running,)).start()

a = [0]
Thread(target=test, args=(a,)).start()

while running[0]:
    print(a[0])
