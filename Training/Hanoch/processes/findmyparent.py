import argparse
import psutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--process_name')
    args = parser.parse_args()
    process = ''
    for p in psutil.process_iter():
        if p.name().lower() == args.process_name:
            process = p
    if process:
        parent = process.parent()
        if parent:
            print(parent.name())
        else:
            print('no parent process!')
    else:
        print('no such process!')
    
if __name__ == '__main__':
    main()