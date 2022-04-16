import os
import sys
import time

from win32 import win32api
from win32 import win32process
from win32 import win32gui

# These functions serve the purpose of hiding the program from the user such
# that it can continue to run in the background with the user's knowledge

def callback(hwnd, pid):
  if win32process.GetWindowThreadProcessId(hwnd)[1] == pid:
    win32gui.ShowWindow(hwnd, 0)

def hide():
    win32gui.EnumWindows(callback, os.getppid())


# This commented out method does not work as it hides the window in the
#  foreground, not neccessarily this program

# import win32gui, win32con
# # Hides command-line window
# def hide():
#     console = win32gui.GetForegroundWindow()
#     win32gui.ShowWindow(console, win32con.SW_HIDE)