import os
import sys
import time
import webbrowser
from pynput.keyboard import Key, Controller


# Called when command phrase is heard, executes various functionalities
# Input: String
def va_commands(phrase):
  command = phrase.split()[0]
  # Play and stop are interchangable since they use the same keystroke
  if command == "play":
    controller = Controller()
    controller.tap(Key.media_play_pause)
  elif command == "stop":
    controller = Controller()
    controller.tap(Key.media_play_pause)
  # Common voice assistant capabilities, search queries, questions
  elif command == "search":
    query = "https://www.google.com/search?q="
    for word in phrase.split()[1:]:
      query += (word + "+")
    webbrowser.open_new(query)
  elif command == "what":
    query = "https://www.google.com/search?q="
    for word in phrase.split()[0:]:
      query += (word + "+")
    webbrowser.open_new(query)
  elif command == "how":
    query = "https://www.google.com/search?q="
    for word in phrase.split()[0:]:
      query += (word + "+")
    webbrowser.open_new(query)
  elif command == "where":
    query = "https://www.google.com/search?q="
    for word in phrase.split()[0:]:
      query += (word + "+")
    webbrowser.open_new(query)
  elif command == "when":
    query = "https://www.google.com/search?q="
    for word in phrase.split()[0:]:
      query += (word + "+")
    webbrowser.open_new(query)
  # Only added capabilities to open youtube and gmail, easily expanded
  elif command == "open":
    query = phrase.split()[1]
    if query == "youtube":
      webbrowser.open_new("https://www.youtube.com/")
    elif query == "email" or query == "gmail":
      webbrowser.open_new("https://mail.google.com/")

  # My attempt to open external programs (non browser) like spotify and games
  # elif command == "open":
  #   target = " ".join(phrase.split()[1:])
  #   controller.press(Key.cmd)
  #   controller.press('s')
  #   controller.release(Key.cmd)
  #   controller.release('s')
  #   print(target)
  #   prog = list(target)
  #   for letter in prog:
  #     controller.tap(letter)
  #   controller.tap(Key.enter)