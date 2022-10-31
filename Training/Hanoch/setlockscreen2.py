import winreg


ROOT = winreg.HKEY_CURRENT_USER
SUB = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Lock Screen\Creative'


def main():
    path = input('Enter lockscreen image path')
    key = winreg.CreateKeyEx(ROOT, SUB)
    winreg.SetValueEx(key, 'LockScreenImage', 0, winreg.REG_SZ, path)
    winreg.CloseKey(key)

    
if __name__ == '__main__':
    main()