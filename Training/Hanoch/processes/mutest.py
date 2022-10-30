import msvcrt
import os
import time


FILE_PATH = r'C:\Users\moshiko\Hafifa\Training\Hanoch\processes\test.txt'


def main():
    line = 'This should be here'
    file = open(FILE_PATH, 'w')
    start_pos  = file.tell()
    print('process 1 locking file for 10 seconds...')
    msvcrt.locking(file.fileno(), msvcrt.LK_NBRLCK, len(line))
    time.sleep(10)
    file.write(line)
    end_pos = file.tell()
    file.seek(start_pos)
    msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, len(line))
    file.seek(end_pos)
    print('process 1 unlocked file.')
    file.close()
    
    
if __name__ == '__main__':
    main()