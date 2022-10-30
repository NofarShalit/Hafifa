import win32event
import win32con


def main():
    try:
        win32event.OpenMutex(win32con.SYNCHRONIZE, False, "MyMutex")
    except:
        print("MyMutex does not exist")
    else:
        print("MyMutex exists")

    
if __name__ == '__main__':
    main()