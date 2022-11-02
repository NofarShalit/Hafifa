#include <windows.h>
#include <winreg.h>
#include <stdio.h>
#include <string.h>

int main()
{
    HKEY ROOT_KEY = "HKEY_LOCAL_MACHINE";
    LPCWSTR SUB_KEY = L"SOFTWARE\\Policies\\Microsoft\\Windows\\Personalization";
    HKEY OPEN_KEY;
    PFILETIME LAST_WRITE_TIME = "";
    LPWSTR lpClass = L"";
    LPDWORD L1 = 0, L2 = 0, L3 = 0, L4 = 0, L5 = 0, L6 = 0, L7 = 0, L8 = 0, L9 = 0;
    RegOpenKeyEx(ROOT_KEY, SUB_KEY, 0, KEY_ALL_ACCESS, &OPEN_KEY);
    RegQueryInfoKey(OPEN_KEY, lpClass, L1, L2, L3, L4, L5, L6, L7, L8, L9, &LAST_WRITE_TIME);
    FILETIME ft;
    SYSTEMTIME st;
    printf("%x", &LAST_WRITE_TIME);

    return 0;
}