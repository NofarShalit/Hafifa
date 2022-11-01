import winreg


ROOT = winreg.HKEY_LOCAL_MACHINE
SUB = r'SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP'


def main():
    
    # C:\Users\moshiko\Downloads\1200px-Coat_of_arms_of_Ramat_Gan.svg.png
    path = input('Enter lockscreen image path')
    key = winreg.CreateKeyEx(ROOT, SUB)
    winreg.SetValueEx(key, 'LockScreenImagePath', 0, winreg.REG_SZ, path)
    winreg.SetValueEx(key, 'LockScreenImageUrl', 0, winreg.REG_SZ, path)
    winreg.SetValueEx(key, 'LockScreenImageStatus', 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

    
if __name__ == '__main__':
    main()