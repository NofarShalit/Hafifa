import win32clipboard, time


MENU = '''
1 - get clipboard contents
2 - set clipboard contents
3 - lock clipboard
4 - exit

Pick an option:
'''
def main():
    choice = input(MENU)
    while choice != '4':
        if choice == '1':
            win32clipboard.OpenClipboard()
            cbdata = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print(cbdata)
        elif choice == '2':
            text = input('Enter your text: ')
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(text)
            win32clipboard.CloseClipboard()
        elif choice == '3':
            print('h')
            win32clipboard.OpenClipboard()
            time.sleep(1000)
        else:
            print('\nERROR, TRY AGAIN\n')
        choice = input(MENU)
if __name__ == '__main__':
    main()