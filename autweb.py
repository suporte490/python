import pyautogui
import time


 
pyautogui.press("win")
pyautogui.click(x=1296, y=82)
time.sleep(2)
pyautogui.write ("google chrome")
time.sleep(2)
pyautogui.click(x=1117, y= 202)
time.sleep(2)
pyautogui.hotkey("ctrl","t")
time.sleep(2)
pyautogui.write("https://www.instagram.com/p/CdCfKmqjtfT/")
time.sleep(2)
pyautogui.press("enter")


