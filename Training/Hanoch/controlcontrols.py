import pyHook
import win32con
import win32api
import pythoncom
import threading
import itertools
import keyboard


MENU = '''
WELCOME TO THE TROLLAGE
1 - LOCK IT ALL
2 - LOCK MOUSE
3 - LOCK KEYBOARD
4 - SWITCH MOUSE BUTTONS
5 - LOSER KEYBOARD

PICK YOUR POISON: 
'''
SENTENCE = itertools.cycle('I AM A LOSER ')
called_by_hook_mouse = False
called_by_hook_keyboard = False


def block(event):
    return False


def left_down(event):
    global called_by_hook_mouse
    if called_by_hook_mouse:
        called_by_hook_mouse = False
        return True
    else:
        t = threading.Thread(target=win32api.mouse_event,args=(win32con.MOUSEEVENTF_LEFTDOWN,0,0))
        t.start()
        called_by_hook_mouse = True
        return False


def left_up(event):
    global called_by_hook_mouse
    if called_by_hook_mouse:
        called_by_hook_mouse = False
        return True
    else:
        t = threading.Thread(target=win32api.mouse_event,args=(win32con.MOUSEEVENTF_LEFTUP,0,0))
        t.start()
        called_by_hook_mouse = True
        return False


def right_down(event):
    global called_by_hook_mouse
    if called_by_hook_mouse:
        called_by_hook_mouse = False
        return True
    else:
        t = threading.Thread(target=win32api.mouse_event,args=(win32con.MOUSEEVENTF_RIGHTDOWN,0,0))
        t.start()
        called_by_hook_mouse = True
        return False


def right_up(event):
    global called_by_hook_mouse
    if called_by_hook_mouse:
        called_by_hook_mouse = False
        return True
    else:
        t = threading.Thread(target=win32api.mouse_event,args=(win32con.MOUSEEVENTF_RIGHTUP,0,0))
        t.start()
        called_by_hook_mouse = True
        return False


def type_key(event):
    global called_by_hook_keyboard
    if called_by_hook_keyboard:
        called_by_hook_keyboard = False
        return True
    else:
        c = SENTENCE.__next__()
        called_by_hook_keyboard = True
        keyboard.write(c)
        return False

    
def main():
    choice = input(MENU)
    hm = pyHook.HookManager()
    if choice == '2' or choice == '1':
        hm.MouseAllButtons = block
    if choice == '3' or choice == '1':
        hm.KeyAll = block
    elif choice == '4':
        hm.MouseLeftDown = right_down
        hm.MouseRightDown = left_down
        hm.MouseLeftUp = right_up
        hm.MouseRightUp = left_up
    elif choice == '5':
        hm.KeyDown = type_key
        hm.KeyUp = block
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    hm.UnhookMouse()
    hm.UnhookKeyboard()


if __name__ == '__main__':
    main()

