import pyautogui
from pyautogui import *
import time
from win32api import GetSystemMetrics
metrics = [GetSystemMetrics(0), GetSystemMetrics(1)]


class AdwCleanerClean:
    i_agree = [360, 373]  # Location of the I Agree button constant
    scan = [416, 218]  # Location of the Scan Now button Constant
    exit_button = [702, 0]
    corner_button = [602, 425]
    correct_blue_value = 174

    @classmethod
    def adw_cleaner_run(cls):
        time.sleep(2)
        print("Started")
        result = pyautogui.confirm("Click OK if 1. AdwCleaner is open, 2. All other apps are closed.")
        if result == "Cancel":
            exit(0)
        print("Confirmed")
        # Find top left bug icon
        cls.tap_i_agree(locate_image("bug"))
        cls.tap_scan(locate_image("bug"))
        time.sleep(5)  # Wait for clean
        coord = locate_image("bug")
        check_for_blue_screenshot = pyautogui.screenshot(region=(coord[0], coord[1], metrics[0], metrics[1]))
        pixel_at_corner = check_for_blue_screenshot.getpixel((
            (coord[0] + cls.corner_button[0]), (coord[1] + cls.corner_button[1])
        ))
        while pixel_at_corner[2] is not cls.correct_blue_value:  # Waits until done
            time.sleep(3)  # Wait before trying again
            coord = locate_image("bug")
            # Screenshot of smaller area to save resources
            check_for_blue_screenshot = pyautogui.screenshot(region=(coord[0], coord[1], metrics[0], metrics[1]))
            pixel_at_corner = check_for_blue_screenshot.getpixel(
                ((cls.corner_button[0]), (cls.corner_button[1]))
                # Coordinates are in a smaller size because of screenshot starting at bug icon
            )
            print("Button not blue")
        # Move to Skip/Quarantine & Click
        print("Button IS blue - clicking")
        if locate_image("Ok") is not None:  # If it detects an "Ok" button will click and prompt user
            ok_button_coordinates = locate_image("Ok")
            pyautogui.click(ok_button_coordinates[0], ok_button_coordinates[1])
            pyautogui.alert("Please select all items to quarantine - then press OK")
        coord = locate_image("bug")
        pyautogui.click(coord[0] + cls.corner_button[0], coord[1] + cls.corner_button[1])
        pyautogui.click(coord[0] + cls.exit_button[0], coord[1] + cls.exit_button[1])

    @classmethod
    def tap_i_agree(cls, coord):
        pyautogui.click(coord[0] + cls.i_agree[0], coord[1] + cls.i_agree[1])

    @classmethod
    def tap_scan(cls, coord):
        pyautogui.click(coord[0] + cls.scan[0], coord[1] + cls.scan[1])


def locate_image(image):
    if image == "bug":
        coord = pyautogui.locateCenterOnScreen('buggy.png')
        while coord is None:
            time.sleep(1)
            coord = pyautogui.locateCenterOnScreen(
                'buggy.png', region=(0, 0, GetSystemMetrics(0) / 2, GetSystemMetrics(1) / 2)
            )
    elif image == "Ok":
        coord = pyautogui.locateCenterOnScreen('OK.png')
        return coord
    else:
        alert("That image is not in our list!")
        raise Exception("locate_image was called with an image not in our list!")
    print("Image coordinates located")
    return coord
# ------------------------ END of AdwCleaner ------------------------------------
#
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    AdwCleanerClean().adw_cleaner_run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
