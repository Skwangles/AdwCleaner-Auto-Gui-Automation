import pyautogui
from pyautogui import *
import time
import keyboard
import win32api
import subprocess
from win32api import GetSystemMetrics
iagree = [360, 373] #Location of the I Agree button constant
scan = [416, 218] #Location of the Scan Now button Constant
metrics = [GetSystemMetrics(0), GetSystemMetrics(1)]
def mwb():
    time.sleep(2)
    print("Started")
    subprocess.call(["C:\\Users\\tree_\\Downloads\\adwcleaner_8.3.0.exe"])  #Open adwcleaner
    pyautogui.confirm("Click OK if 1. AdwCleaner is open, 2. All other apps are closed.")
    coord = pyautogui.locateCenterOnScreen("buggy.png", region=(0, 0, GetSystemMetrics(0)/2, GetSystemMetrics(1)/2))  #Find top left bug
    tap_i_agree(coord)
    tap_scan(coord)
    time.sleep(20)  #Wait for clean
    sbr_coords = pyautogui.locateCenterOnScreen("skipb.png", region=(
        coord[0], coord[1], metrics[0], metrics[1]
    ))
    print(sbr_coords)


def tap_i_agree(coord):
    pyautogui.moveTo(coord[0] + iagree[0], coord[1] + iagree[1], duration=0)
    pyautogui.click()


def tap_scan(coord):
    pyautogui.moveTo(coord[0] + scan[0], coord[1] + scan[1], duration=0)
    pyautogui.click()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    mwb()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
