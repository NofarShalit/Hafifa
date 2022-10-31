import winreg
import datetime


def windows_ticks_to_unix_seconds(windows_ticks):
    return windows_ticks/10000000 - 11644473600


def main():
    path = input('Enter key path')
    root = path.split('\\')[0]
    sub = path[len(root) + 1:]
    if root == 'HKLM' or root == 'HKEY_LOCAL_MACHINE':
        root = winreg.HKEY_LOCAL_MACHINE
    elif root == 'HKCU' or root == 'HKEY_CURRENT_USER':
        root = winreg.HKEY_CURRENT_USER
    elif root == 'HKEY_USERS':
        root = winreg.HKEY_USERS
    elif root == 'HKCR' or root == 'HKEY_CLASSES_ROOT':
        root = winreg.HKEY_CLASSES_ROOT
    elif root == 'HKCC' or root == 'HKEY_CURRENT_CONFIG':
        root = winreg.HKEY_CURRENT_CONFIG
    key = winreg.OpenKey(root, sub)
    time = datetime.datetime.fromtimestamp(windows_ticks_to_unix_seconds(winreg.QueryInfoKey(key)[2]))
    print(f'Last modified {time}')
    winreg.CloseKey(key)
    
if __name__ == '__main__':
    main()