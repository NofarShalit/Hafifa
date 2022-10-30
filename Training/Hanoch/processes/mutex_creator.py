import win32event
import time


def main():
    obj = win32event.CreateMutex(None, False, "MyMutex")
    time.sleep(1000)

    
if __name__ == '__main__':
    main()
