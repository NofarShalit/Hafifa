#include <winreg.h>

HKEY ROOT_KEY = "HKEY_LOCAL_MACHINE"
LPCSTR SUB_KEY = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\DiskDiagnostics"
DWORD KEY_ACCESS = "KEY_ALL_ACCESS"
RegOpenKeyExW($ROOT_KEY, $SUB_KEY,0,$KEY_ACCESS,$OPEN_KEY)
RegQueryInfoKeyW($OPEN_KEY,$null,$null,$null,$null,$null,$null,$null,$null,$null,$null,$null,$LAST_WRITE_TIME)
echo $LAST_WRITE_TIME