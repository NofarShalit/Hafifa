import winreg
from datetime import datetime

def WindowsTickToUnixSeconds(WindowsTicks):
    return WindowsTicks/10000000 - 11644473600

def main():
    Path = input("Enter the key path: ")
    RootPath = Path.split("\\")[0]
    SubKey = Path[(len(RootPath)+1):]
    if RootPath == 'HKLM' or RootPath == 'HKEY_LOCAL_MACHINE':
        RootPath = winreg.HKEY_LOCAL_MACHINE
    elif RootPath == 'HKCU' or RootPath == 'HKEY_CURRENT_USER':
        RootPath = winreg.HKEY_CURRENT_USER
    elif RootPath == 'HKEY_USERS':
        RootPath = winreg.HKEY_USERS
    elif RootPath == 'HKCR' or RootPath == 'HKEY_CLASSES_ROOT':
        RootPath = winreg.HKEY_CLASSES_ROOT
    elif RootPath == 'HKCC' or RootPath == 'HKEY_CURRENT_CONFIG':
        RootPath = winreg.HKEY_CURRENT_CONFIG
    Key = winreg.OpenKey(RootPath, SubKey)
    LastModified = datetime.fromtimestamp(WindowsTickToUnixSeconds(winreg.QueryInfoKey(Key)[2]))
    print(f"Last Modified {LastModified}")
    winreg.CloseKey(Key)

if __name__ == "__main__":
    main()