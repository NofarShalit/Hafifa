import pyHook
import time
import win32con
import win32api
import pythoncom


def block(event):
    return False

def ld_to_rd(event):
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    return True

def lu_to_ru(event):
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
    return True

def rd_to_ld(event):
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    return True

def ru_to_lu(event):
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    return True

def main():
    hm = pyHook.HookManager()
    #hm.MouseAll = block
    hm.MouseLeftDown = ld_to_rd
    hm.MouseRightDown = rd_to_ld
    hm.MouseLeftUp = lu_to_ru
    hm.MouseRightUp = ru_to_lu
    #hm.KeyAll = block
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    hm.UnhookMouse()
    hm.UnhookKeyboard()


if __name__ == '__main__':
    main()