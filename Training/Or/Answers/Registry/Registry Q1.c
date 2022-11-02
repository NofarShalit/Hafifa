#include <winreg.h>
#include <stdio.h>
#include <string.h>
#include <windows.h>

int main()
{
    HKEY ROOT_KEY = "HKEY_LOCAL_MACHINE";
    LPCSTR SUB_KEY = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\DiskDiagnostics";
    HKEY OPEN_KEY;
    PFILETIME LAST_WRITE_TIME;
    RegOpenKeyExW(ROOT_KEY, SUB_KEY, 0, KEY_ALL_ACCESS, &OPEN_KEY);
    RegQueryInfoKeyW(OPEN_KEY,0,0,0,0,0,0,0,0,0,0,0,LAST_WRITE_TIME);
    printf(LAST_WRITE_TIME);

    return 0;
}