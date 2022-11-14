import winreg

ROOT_PATH = winreg.HKEY_CURRENT_USER
SUB_KEY = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU'

def main():
    Key = winreg.OpenKeyEx(ROOT_PATH, SUB_KEY)
    Counter = 1
    print("The file types that have been opened are: ")
    while True:
        try:
            print(winreg.EnumKey(Key, Counter), end=", ")
            Counter += 1
        except OSError:
            break
    winreg.CloseKey(Key)

if __name__ == "__main__":
    main()