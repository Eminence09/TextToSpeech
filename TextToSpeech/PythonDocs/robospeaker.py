from win32com.client import Dispatch
import os
speak = Dispatch("SAPI.SpVoice").Speak
op = ("Hello,there how are you? here you can type a text and listen that text Created by yash")
speak(op)
while True:
    text = input("Type something to read aloud:")
     #installs pypiwin32
    if text == "q":
        speak('bye bye bro thank you for visiting to us')
        break
    speak(text)