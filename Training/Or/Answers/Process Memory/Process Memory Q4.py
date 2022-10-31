import psutil

PROCNAME = "Everything.exe"

def main():
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            print(proc)

if __name__ == "__main__":
    main()

"""
from multiprocessing import active_children, Process
from time import sleep

def get_process_by_name(pname):
    processes = active_children()
    for process in processes:
        if process.name == pname:
            return process
    return None

def main():
    print(get_process_by_name("Everything.exe"))

if __name__ == "__main__":
    main()
"""
"""
import subprocess as sub

def get_pid(name):
    return sub.check_output(["pidof ",name])

def main():
    get_pid("Everything.exe")

if __name__ == "__main__":
    main()
"""