import pynput
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener

import pyautogui
import os.path
from datetime import datetime
import time 
import sys
import os
from sys import platform as _platform

try:
    inactivity = float(sys.argv[1])
    interval = float(sys.argv[2])
except IndexError:
    inactivity, interval = 3, 1

#Defining color values for later
G = '\033[32m' #Green
R = '\033[31m' # Red
C = '\033[36m' # Cyan
W = '\033[0m'  # White


#Needs testing but it SHOULD work
if _platform == "linux" or _platform =="linux2" or _platform =="darwin":
    os.system('clear')
elif _platform == "win32" or _platform == "win64":
        os.system('cls')


class Counter:

    def __init__(self):
        self.time_point = time.time()

    def reset(self):
        self.time_point = time.time()

    def get_count(self):
        return time.time() - self.time_point


count_interval = Counter()
count_inactivity = Counter()


def press_escape():
    print(".")
    pyautogui.press('enter')


try:
    print(G + f"Press escape every {interval}s after {inactivity}s inactivity..." + W)

    def other(*args):
        count_inactivity.reset()

    with Listener(on_press=other, on_release=other), MouseListener(on_move=other, on_click=other, on_scroll=other):
        while True:
            time.sleep(0.1)

            if count_inactivity.get_count() > inactivity and count_interval.get_count() > interval:
                count_interval.reset()

                # Oops, escape clears inactivity, so lets retrofix this here
                count_inactivity.time_point, _ = (
                    float(count_inactivity.time_point),
                    press_escape()
                )
           
except KeyboardInterrupt:
    print('\n' + R + "Program Killed X_X" + W)
