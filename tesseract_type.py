# with obj recognition
from subprocess import call
import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui
import time
from autocorrect import spell
import string




screen_shot = mss()

# portion of screen shot


def take_screenshot(mon={"top": 720, "left": 410, "width": 620, "height": 145}):
    screen_shot.get_pixels(mon)
    img = Image.frombytes("RGB", (screen_shot.width, screen_shot.height), screen_shot.image)

    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)




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
                ("—",""),
                ("(ech","tech"),
                ("c(i", "cti"),
                ("(hey", "they"),
                ("Bux", "But"),
                ("Khe", "the"),
                ("zou", "you"),
                ("nox", "not"),
                ("oxher", "other"),
                ("resx", "rest"),
                ("targex", "target"),
                ("exgerience", "experience"),
                ("outpux", "output"),
                ("ax", "at"),
                ("haul", "hour"),
                ("czclone", "cyclone")]


def clean_typos(text):
    cleaned_text = text
    for pair in common_typos:
        cleaned_text = cleaned_text.replace(pair[0],pair[1])

    return cleaned_text


debug_file = open("debug_file.txt", "a")


# spell checks each word (except for contractions) and preserves punctuation

def spell_check(str):
    str_list = str.split()
    result_list = []

    for word in str_list:
        if word.find("'") == -1 and word.find("‘") == -1:
            if word[-1] == "." or word[-1] == ",":
                result_list.append(spell(word[:-1]) + word[-1])
            else:
                result_list.append(spell(word))
        else:
            result_list.append(word)
    return " ".join(result_list)


input("Press enter to start")
time.sleep(2)


iter = 0
prev_text = ""
speed = 0.051
while(True):
    iter += 1

    if iter == 6:
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.scroll(300)
        pyautogui.scroll(-8)
        iter = 0





    cv2.imwrite("picture.png", take_screenshot())

    call(["tesseract", "picture.png", "read_this", "--psm 6"])


    with open("read_this.txt", "r") as file:
        type_out = file.read()

    type_out = clean_typos(type_out)

    print("\n\n" + type_out)

    if type_out == prev_text and speed > 0.01:
        speed -= 0.02
    prev_text = type_out[:]
    pyautogui.typewrite(type_out, interval=speed)
    for str in (string.ascii_lowercase + string.ascii_uppercase):
        pyautogui.press(str)
    pyautogui.press(".")
    pyautogui.press(",")
    pyautogui.press("'")
    pyautogui.press("‘")
    pyautogui.press(" ")


    debug_file.write("\n" + type_out)
