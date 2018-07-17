# with obj recognition
from subprocess import call
import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui
import time



screen_shot = mss()

# portion of screen shot
mon = {"top": 725, "left": 410, "width": 620, "height": 145}


def take_screenshot(mon={"top": 725, "left": 410, "width": 620, "height": 145}):
    screen_shot.get_pixels(mon)
    img = Image.frombytes("RGB", (screen_shot.width, screen_shot.height), screen_shot.image)

    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #img = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)



    return img


common_typos = [("\n"," "),
                ("frmn", "from"),
                ("_", ""),
                (" L ", ""),
                ("Ihey", "They"),
                ("@", ""),
                ("¥", ""),
                ("\"men", "When"),
                ("\"hen", "When"),
                ("1arge", "large"),
                ("smalle", "smaller"),
                ("‘", "."),
                ("—",""),
                ("(ech","tech"),
                ("c(i", "cti"),
                ("(hey", "they"),
                ("Bux", "But")]


def clean_typos(text):
    cleaned_text = text
    for pair in common_typos:
        cleaned_text = cleaned_text.replace(pair[0],pair[1])

    return cleaned_text


debug_file = open("debug_file.txt", "a")




input("Press enter to start")
time.sleep(2)
while(True):

    pyautogui.press(".")
    pyautogui.press(",")
    pyautogui.press("\'")
    pyautogui.press(" ")
    pyautogui.press("t")
    pyautogui.press("T")
    pyautogui.press("enter")



    cv2.imwrite("picture.png", take_screenshot())

    call(["tesseract", "picture.png", "read_this", "--psm 6"])


    with open("read_this.txt", "r") as file:
        type_out = file.read()

    type_out = clean_typos(type_out)


    delay = set_delay()
    pyautogui.typewrite(type_out, interval=0.09)

    debug_file.write("\n" + type_out)
