#include <winreg.h>
#include <stdio.h>
#include <string.h>
#include <windows.h>

int main()
{
    HKEY ROOT_KEY = "HKEY_LOCAL_MACHINE";
    LPCSTR SUB_KEY = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\DiskDiagnostics";
    HKEY OPEN_KEY;
    PFILETIME LAST_WRITE_TIME;
    LPWSTR lpClass;
    LPDWORD L1,L2,L3,L4,L5,L6,L7,L8,L9;
    RegOpenKeyEx(ROOT_KEY, SUB_KEY, 0, KEY_ALL_ACCESS, &OPEN_KEY);
    RegQueryInfoKey(OPEN_KEY,lpClass,L1,L2,L3,L4,L5,L6,L7,L8,L9,LAST_WRITE_TIME);
    printf("%s",LAST_WRITE_TIME);

    return 0;
}