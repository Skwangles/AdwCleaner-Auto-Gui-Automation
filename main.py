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
correct_blue_value = 174

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
    tap_i_agree(locate_image("bug"))
    tap_scan(locate_image("bug"))
    time.sleep(5)  # Wait for clean
    coord = locate_image("bug")
    check_for_blue_screenshot = pyautogui.screenshot(region=(coord[0], coord[1], metrics[0], metrics[1]))
    pixel_at_corner = check_for_blue_screenshot.getpixel(((coord[0] + corner_button[0]), (coord[1] + corner_button[1])))
    while pixel_at_corner[2] is not correct_blue_value:  # Waits until done
        time.sleep(3)  # Wait before trying again
        coord = locate_image("bug")
        # Screenshot of smaller area to save resources
        check_for_blue_screenshot = pyautogui.screenshot(region=(coord[0], coord[1], metrics[0], metrics[1]))
        pixel_at_corner = check_for_blue_screenshot.getpixel(
            ((corner_button[0]), (corner_button[1]))
            # Coordinates are in a smaller size because of screenshot starting at bug icon
        )
        print("Button not blue")
    # Move to Skip/Quarantine & Click
    print("Button IS blue - clicking")
    if locate_image("Ok") is not None:  # If it detects an "Ok" button will click and prompt user
        ok_coords = locate_image("Ok")
        pyautogui.click(ok_coords[0], ok_coords[1])
        pyautogui.alert("Please select all items to quarantine - then press OK")

    pyautogui.click(locate_image("bug")[0] + corner_button[0], locate_image("bug")[1] + corner_button[1])


def locate_image(image):
    if image is "bug":
        coord = pyautogui.locateCenterOnScreen('buggy.png')
        while coord is None:
            time.sleep(1)
            coord = pyautogui.locateCenterOnScreen(
                'buggy.png', region=(0, 0, GetSystemMetrics(0) / 2, GetSystemMetrics(1) / 2)
            )
    elif image is "Ok":
        coord = pyautogui.locateCenterOnScreen('OK.png')
        return coord
    else:
        alert("That image is not in our list!")
        raise Exception("locate_image was called with an image not in our list!")
    print("Image coordinates located")
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
