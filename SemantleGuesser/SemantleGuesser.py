#This program generates random words to help the user play the online game Semantle.
#Semantle is a variation of Wordle. 
#However, the user earns more points by guessing words which are closest in semantic meaning to the target word.
    #ex. If the target word is "turkey", the user will get a higher score from "bird" than "desk"
#The program does not learn from previous inputs at all. It cannot see the scores of the words it enters.
#The user may use hotkeys to enter 1, 10, or 100 words at a time.
#Words may be taken from the list of 3,000 most common English words (reccomended) or
    #the large list of all English words (risky, as Semantle does not recognize many of those)

#List of 3,000 most common English words taken from https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/
#List of all English words taken from https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt



import random
import pyautogui
import keyboard
from pynput.keyboard import Listener, KeyCode
import win32api
import win32con
from pynput.mouse import Controller, Button
import threading
import time


STOP_KEY = KeyCode(char = "`")

GUESS_ONCE = KeyCode(char = "[")
GUESS_TEN = KeyCode(char = "]")
GUESS_HUNDRED = KeyCode(char = "\\")
WORD_LENGTH_CAP = 7 #only really needs to be used for wordsBig.txt

def load_words():
    with open('wordsCommon.txt') as word_file: #list of the 3,000 most common English words
        semi_valid_words = set(word_file.read().split())
        valid_words = set()

        #UNCOMMENT THE FOLLOWING CODE IF YOU WISH TO MANUALLY ADD A WORD LENGTH CAP (also must return valid_words instead of semi_valid_words
        #-----------------------------------------------------------------------------------
        #for word in semi_valid_words:
        #    if len(word) <= WORD_LENGTH_CAP:
        #        valid_words.add(word)
        #-----------------------------------------------------------------------------------

    #return valid_words
    return semi_valid_words


def guesser():
    global english_words
    english_words = load_words()
    global guessing
    guessing = True

def toggleEvent(key):
    global guessing

    
    if key == GUESS_ONCE:
        pyautogui.write("\b") #backspace
        pyautogui.write(english_words.pop())
        time.sleep(0.2)
    if key == GUESS_TEN:
        pyautogui.write("\b")
        for i in range (11):
            if guessing:
                pyautogui.write(english_words.pop())
                time.sleep(0.01)
                keyboard.press('enter')
                time.sleep(0.10)
    if key == GUESS_HUNDRED:
        pyautogui.write("\b")
        for i in range (101):
            if guessing:
                pyautogui.write(english_words.pop())
                time.sleep(0.01)
                keyboard.press('enter')
                time.sleep(0.10)

jump_thread = threading.Thread(target = guesser)
jump_thread.start()

with Listener(on_press = toggleEvent) as listener:
    listener.join()

