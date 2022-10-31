import winreg


ROOT = winreg.HKEY_LOCAL_MACHINE
SUB = r'SOFTWARE\Policies\Microsoft\Windows\Personalization'


def main():
    path = input('Enter lockscreen image path')
    key = winreg.CreateKeyEx(ROOT, SUB)
    winreg.SetValueEx(key, 'LockScreenImage', 0, winreg.REG_SZ, path)
    winreg.CloseKey(key)

    
if __name__ == '__main__':
    main()