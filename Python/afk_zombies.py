#!/usr/bin/python

import pyautogui
import sys
import time

pyautogui.FAILSAFE = True

time.sleep(10)

try:
    while True:

        pyautogui.mouseDown(button='right')
        time.sleep(10)
        pyautogui.mouseUp(button='right')
        time.sleep(.5)
        pyautogui.click()

except KeyboardInterrupt:
    print('Exiting...')
    sys.exit(0)
