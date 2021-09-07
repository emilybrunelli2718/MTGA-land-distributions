import pyautogui
import time
#Instructions: start up MTGA. Run bot_match.py. Quickly go back to MTGA.
def concede():
    pyautogui.moveTo(960, 630)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

def mulligan():
    pyautogui.moveTo(790, 870)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

def play_bot():
    pyautogui.moveTo(1740,990)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

def options():
    pyautogui.moveTo(1879, 25)
    pyautogui.mouseDown()
    time.sleep(.2)
    pyautogui.mouseUp()

def bot_match(matches):
    time.sleep(5)
    for i in range(matches):
        play_bot()
        time.sleep(2)
        play_bot()
        time.sleep(15)

        for j in range(7):
            mulligan()
            time.sleep(1.8)

        options()
        time.sleep(1)
        concede()
        time.sleep(8)
        concede()
        time.sleep(20)


bot_match(1000)
