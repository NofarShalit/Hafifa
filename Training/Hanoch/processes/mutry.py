import msvcrt
import os
import time


FILE_PATH = r'C:\Users\moshiko\Hafifa\Training\Hanoch\processes\test.txt'


def main():
    line = 'This should not be here'
    file = open(FILE_PATH, 'w')
    start_pos = file.tell()
    try:
        print('process 2 trying to write to file...')
        msvcrt.locking(file.fileno(), msvcrt.LK_NBRLCK, len(line))
        file.write(line)
        end_pos = file.tell()
        file.seek(start_pos)
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, len(line))
        file.seek(end_pos)
    except OSError:
        print('process 2 unable to open.')
    finally:
        file.close()
        
    
    
    
if __name__ == '__main__':
    main()