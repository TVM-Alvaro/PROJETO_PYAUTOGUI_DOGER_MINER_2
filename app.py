import pyautogui
from time import sleep

pyautogui.moveTo(1375,-592,duration=2)
for i in range (1349):
    sleep(0.1)
    pyautogui.click()