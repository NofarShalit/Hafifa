import win32event, pywintypes
import time

def main():

    STANDARD_RIGHTS_REQUIRED = 0xF0000
    SYNCHRONIZE = 0x100000
    MUTANT_QUERY_STATE = 0x1
    MUTEX_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | MUTANT_QUERY_STATE
    
    OpenMutex = win32event.OpenMutex(MUTEX_ALL_ACCESS,pywintypes.FALSE,"Bazinga")

if __name__ == "__main__":
    main()