import pyautogui
from time import sleep

sleep(3)
n = int(input())
for i in range(1, n + 1):
    row = "#" * i
    pyautogui.write(row)
    pyautogui.press("enter")
