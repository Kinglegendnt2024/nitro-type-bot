# nitro-type-bot
Created a bot to play nitro type using tesseract OCR
Requires tesseract-ocr installed




The file brute_force.py was an early control group-style of attempt at doing nitro type. The hope was that it would spam all
the keys required quick enough to actually get through the text but the game requires accuracy to be above 50% after the first
few words.

tesseract_type.py is the actual bot. It takes a screenshot with mss module at the area of the screen specified by mon. That
image is then passed to tesseract through terminal commands executed by the code with the subprocess module. Tesseract writes
the text it deciphers to the read_this.file. The python program reads this file in, cleans it up a bit, including some hard
coded fixes for the errors tesseract make. Then it types it out using pyautogui
