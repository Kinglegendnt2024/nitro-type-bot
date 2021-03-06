# with obj recognition
from autocorrect import spell
from subprocess import call
from PIL import Image
from mss import mss
import numpy as np
import pyautogui
import string
import time
import cv2

screen_shot = mss()

# crop screenshot of screen so it is only the textbox of nitrotype
def return_screenshot(mon={"top": 720, "left": 410, "width": 620, "height": 145}):
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

# spell checks each word (except for contractions) using the spell check module and preserves punctuation
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
SPEED = 0.081 # how fast the letters are typed
iter = 0

while(True):
    iter += 1

    if iter == 6:
        pyautogui.press("enter")
        time.sleep(20)
        pyautogui.scroll(300)
        time.sleep(0.1)
        pyautogui.scroll(-8)
        iter = 0

    # write out the screenshot of the text box
    cv2.imwrite("picture.png", return_screenshot())

    # bash call for tessract to analyze image
    call(["tesseract", "picture.png", "read_this", "--psm 6"])

    # read analyzed picture-text back in 
    with open("read_this.txt", "r") as file:
        type_out = file.read()

    type_out = clean_typos(type_out)

    print("\n\n" + type_out)

    # type the text into the game
    pyautogui.typewrite(type_out, interval=SPEED)
    # type random characters to account for messing up.
    pyautogui.typewrite(string.ascii_lowercase + string.ascii_uppercase)
    pyautogui.typewrite(".,'‘ ")

    # keeping a log of what tesseract outputs.
    with open("debug_file.txt", "a") as file:
        file.write("\n" + type_out)
