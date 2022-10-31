import win32event, win32con
import time

def main():
    try:
        win32event.OpenMutex(win32con.SYNCHRONIZE,1,"MutexBazinga")
        print("MutexBazinga Exists")
    except:
        print("MutexBazinga Doesn't Exists")

if __name__ == "__main__":
    main()