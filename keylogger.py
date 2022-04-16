import os
import sys
import time
import webbrowser
from datetime import datetime
from pynput.keyboard import Key, Controller
from pynput import keyboard
import speech_recognition as sr
from gtts import gTTS

last_keystroke = datetime.now()

def on_press(key):
    try:
        # print('key {0} pressed'.format(
        #     key.char))
        key_logger('{0}'.format(key.char))
    except AttributeError:
        # print('{0} pressed'.format(
        #     key))
        user_input = '({0})'.format(key)
        if user_input == ("(Key.space)"):
          key_logger(" ")
        elif user_input == ("(Key.shift)"):
          pass
        else:
          key_logger(user_input)

def key_logger(key_string):
  # Logs every keystroke by the user, starts a new line within the log every
  # minute so analysing the data is simpler
  global last_keystroke
  dateTimeObj = datetime.now()
  f = open("key.txt", "a")
  if (dateTimeObj - last_keystroke).total_seconds() > 60:
    last_keystroke = dateTimeObj
    date_time = dateTimeObj.strftime("%d/%m/%Y, %H:%M")
    f.write("\n")
    f.write("(" + date_time + ")")
  f.write(key_string)
  f.close()