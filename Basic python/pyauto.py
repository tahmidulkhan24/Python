import pyautogui
from time import sleep

sleep(5)
for i in range(1, 20):
    pyautogui.write("chi badhan", interval=0.25)
    pyautogui.press("enter")
