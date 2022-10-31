import winreg


ROOT = winreg.HKEY_CURRENT_USER
SUB = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU'
def main():
    key = winreg.OpenKeyEx(ROOT, SUB)
    i = 1
    while True:
        try:
            print(winreg.EnumKey(key, i))
            i += 1
        except OSError:
            break
    winreg.CloseKey(key)
if __name__ == '__main__':
    main()