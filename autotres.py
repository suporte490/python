import pyautogui
import time


pyautogui.click(x=78, y=747)
pyautogui.hotkey("ctrl", "t")
time.sleep(2)
pyautogui.write("https://www.youtube.com/shorts/mMME1gaDNDc")
pyautogui.press("enter")


