# with obj recognition
from subprocess import call
import numpy as np
import cv2
from mss import mss
from PIL import Image
import keyboard
import pyautogui
import time



screen_shot = mss()

# portion of screen shot
mon = {"top": 710, "left": 470, "width": 500, "height": 120}


def take_screenshot():
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
                ("\"hen", "When") ]


def clean_typos(text):
    cleaned_text = text
    for pair in common_typos:
        cleaned_text = cleaned_text.replace(pair[0],pair[1])

    return cleaned_text

keyboard.on_press_key("escape", lambda _: exit(), suppress=False)


for _ in range(5):
    time.sleep(1.5)

    cv2.imwrite("picture.png", take_screenshot())

    call(["tesseract", "picture.png", "read_this", "--psm 6"])


    with open("read_this.txt", "r") as file:
        type_out = file.read()

    type_out = clean_typos(type_out)



    pyautogui.typewrite(type_out, interval=0.0001)


    print("\n" + str(type_out))
