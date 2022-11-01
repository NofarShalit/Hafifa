import psutil

PROCNAME = "dwm.exe"

def main():
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            for pproc in psutil.process_iter():
                if proc.ppid() == pproc.pid:
                    print(pproc.name())

if __name__ == "__main__":
    main()