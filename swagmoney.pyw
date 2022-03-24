import os
import time

os.system('py -m pip install playsound')
time.sleep(2)
os.system('py -m pip install pynput')

from playsound import playsound
from pynput.mouse import Listener

def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    try:
        playsound('boom.mp3')
    except:
        pass

def on_scroll(x, y, dx, dy):
    pass

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()











