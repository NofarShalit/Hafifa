import pyHook
import time
import win32con
import win32api
import pythoncom
import threading
import itertools
import keyboard


MENU = '''
WELCOME TO THE TROLLAGE
1 - LOCK MOUSE
2 - LOCK KEYBOARD
3 - SWITCH MOUSE BUTTONS
4 - PLANT SENTENCE INTO KEYBOARD

PICK YOUR POISON: 
'''
SENTENCE = itertools.cycle('i am a loser ')



def block(event):
    return False

def right_down(event):
    t = threading.Thread(target=win32api.mouse_event, args=(win32con.MOUSEEVENTF_RIGHTDOWN,0,0))
    t.start()
    return False

def right_up(event):
    t = threading.Thread(target=win32api.mouse_event, args=(win32con.MOUSEEVENTF_RIGHTUP,0,0))
    t.start()
    return False

def left_down(event):
    t = threading.Thread(target=win32api.mouse_event, args=(win32con.MOUSEEVENTF_LEFTDOWN,0,0))
    t.start()
    return False

def left_up(event):
    t = threading.Thread(target=win32api.mouse_event, args=(win32con.MOUSEEVENTF_LEFTUP,0,0))
    t.start()
    return False

def type_key(event):
    c = SENTENCE.__next__()
    keyboard.write(c)
    return False

 
def main():
    choice = input(MENU)
    hm = pyHook.HookManager()
    if choice == '1':
        hm.MouseAllButtons = block
    elif choice == '2':
        hm.KeyAll = block
    elif choice == '3':
        #hm.MouseLeftDown = right_down
        hm.MouseRightDown = left_down
        #hm.MouseLeftUp = right_up
        hm.MouseRightUp = left_up
    elif choice == '4':
        hm.KeyDown = type_key
        hm.KeyUp = block
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    hm.UnhookMouse()
    hm.UnhookKeyboard()

if __name__ == '__main__':
    main()
