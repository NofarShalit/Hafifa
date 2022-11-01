import psutil

PROCNAME = "Everything.exe"

def main():
    for proc in psutil.process_iter():
        if proc.name().lower() == PROCNAME:
            print(proc)

if __name__ == "__main__":
    main()