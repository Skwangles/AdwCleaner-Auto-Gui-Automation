import pyautogui
from pyautogui import *
import time
import keyboard
import win32api
import subprocess
from win32api import GetSystemMetrics

i_agree = [360, 373]  # Location of the I Agree button constant
scan = [416, 218]  # Location of the Scan Now button Constant
corner_button = [602, 425]
metrics = [GetSystemMetrics(0), GetSystemMetrics(1)]
bottom_right_blue = 174

#
#
# -------------------------AdwCleaner-----------------------------
#
#


def adw_cleaner_run():
    time.sleep(2)
    print("Started")
    pyautogui.confirm("Click OK if 1. AdwCleaner is open, 2. All other apps are closed.")
    # Find top left bug icon
    tap_i_agree(find_bug())
    tap_scan(find_bug())
    time.sleep(5)  # Wait for clean
    # pyautogui.moveTo(find_bug()[0] + corner_button[0], find_bug()[1] + corner_button[1], duration=3)
    # time.sleep(3)
    # pyautogui.moveTo(30, 30, duration=0)
    coord = find_bug()
    find_blue_screenshot = pyautogui.screenshot(region=(coord[0], coord[1], metrics[0], metrics[1]))
    pixel_at_corner = find_blue_screenshot.getpixel(((coord[0] + corner_button[0]), (coord[1] + corner_button[1])))
    while pixel_at_corner[2] != bottom_right_blue:  # Waits until done
        time.sleep(3)
        coord = find_bug()
        find_blue_screenshot = pyautogui.screenshot(region=(coord[0], coord[1], metrics[0], metrics[1]))
        pixel_at_corner = find_blue_screenshot.getpixel(((corner_button[0]),
                                                         (corner_button[1])))
        print("Button not blue")
    # Move to Skip/Quarantine & Click
    print("Button IS blue - clicking")
    pyautogui.click(find_bug()[0] + corner_button[0], find_bug()[1] + corner_button[1])


def find_bug():
    coord = pyautogui.locateCenterOnScreen('buggy.png')
    while coord is None:
        time.sleep(1)
        coord = pyautogui.locateCenterOnScreen('buggy.png',
                                               region=(0, 0, GetSystemMetrics(0) / 2, GetSystemMetrics(1) / 2))
    print("Icon found")
    return coord


def tap_i_agree(coord):
    pyautogui.click(coord[0] + i_agree[0], coord[1] + i_agree[1])


def tap_scan(coord):
    pyautogui.click(coord[0] + scan[0], coord[1] + scan[1])
#
# ------------------------ END of AdwCleaner ------------------------------------
#

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    adw_cleaner_run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
