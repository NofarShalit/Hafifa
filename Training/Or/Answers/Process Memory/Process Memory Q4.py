import subprocess as sub

def get_pid(name):
    return sub.check_output(["pidof ",name])

def main():
    get_pid("Everything.exe")

if __name__ == "__main__":
    main()