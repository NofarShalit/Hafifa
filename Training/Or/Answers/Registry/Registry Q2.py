import winreg

ROOT = winreg.HKEY_LOCAL_MACHINE
SUB_KEY = r'SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP'

def main():
    ImagePath = input("Enter image path: ")
    Key = winreg.CreateKeyEx(ROOT, SUB_KEY)
    winreg.SetValueEx(Key, 'LockScreenImagePath', 0, winreg.REG_SZ, ImagePath)
    winreg.SetValueEx(Key, 'LockScreenImageUrl', 0, winreg.REG_SZ, ImagePath)
    winreg.SetValueEx(Key, 'LockScreenImageStatus', 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(Key)

if __name__ == "__main__":
    main()