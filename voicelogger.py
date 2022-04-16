import os
import sys
import time
from datetime import datetime

# Takes the transcribed audio and notes it down in an external file along with
# time stamp
# Input: String
def voice_logger(transcribed_audio):
  dateTimeObj = datetime.now()
  f = open("voice.txt", "a")
  date_time = dateTimeObj.strftime("%d/%m/%Y, %H:%M:%S")
  f.write("(" + date_time + ")")
  f.write(" " + transcribed_audio + "\n")
  f.close()

if __name__ == "__main__":\
  voice_logger("Testing String")