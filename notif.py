import os
import sys
import time
from win10toast import ToastNotifier

def close_notif():
    toaster = ToastNotifier()
    toaster.show_toast("Python",
                    "Python voice assistant has been closed",
                    duration=5)
    return 0

def real_close_notif():
    toaster = ToastNotifier()
    toaster.show_toast("Hackerman",
                    "Voicelogger and Keylogger has been closed",
                    duration=5)
    return 0

if __name__ == "__main__":
    close_notif()

# I first tried using Tkinter but this method was blocking and to develop a
#  non blocking Tkinter solution was more complicatied than the above solution

# #For python 3 imports:
# import tkinter as tk
# from tkinter import ttk
# # for python 2 imports:
# # import Tkinter as tk
# # import ttk
# import random

# def popup_spam():
#     root = tk.Tk()
#     root.withdraw()

#     for i in range(0,5):
#         x = tk.Toplevel(root)
#         x.title("Error Box!")
#         x.geometry("300x100+{}+{}".format(random.randint(200,1620), random.randint(200,880)))
#         x.resizable(False, False)
#         ttk.Label(x, text = "Don't delete me please!").pack()
#         ttk.Button(x, text = " OK ", command = x.destroy).pack(side=tk.BOTTOM)

#     root.mainloop()