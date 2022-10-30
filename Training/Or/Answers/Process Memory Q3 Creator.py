from win32event import CreateMutex
import time

def main():
    NewMutex = CreateMutex(None,False,"MutexBazinga")
    print("Created mutex 'MutexBazinga'")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()