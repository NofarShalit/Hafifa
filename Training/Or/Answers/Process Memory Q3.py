from win32event import CreateMutex
import time

def main():
    NewMutex = CreateMutex(None,False,"CreateMutexBazinga")
    while True:
        NewMutex.lock()
        time.sleep(1)

if __name__ == "__main__":
    main()