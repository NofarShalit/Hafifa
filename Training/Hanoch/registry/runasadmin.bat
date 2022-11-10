@echo off

reg add HKEY_CLASSES_ROOT\Python.File\Shell\runas -v "HasLUAShield" -d "" -f >nul
reg add HKEY_CLASSES_ROOT\Python.File\Shell\runas\command -ve -d "\"C:\Users\moshiko\AppData\Local\Microsoft\WindowsApps\python3.10.exe\" \"%%1\"" -f >nul
reg add HKEY_CLASSES_ROOT\VSCode.py\Shell\runas -v "HasLUAShield" -d "" -f >nul
reg add HKEY_CLASSES_ROOT\VSCode.py\Shell\runas\command -ve -d "\"C:\Users\moshiko\AppData\Local\Microsoft\WindowsApps\python3.10.exe\" \"%%1\"" -f >nul
reg add HKEY_CLASSES_ROOT\Thonny.py\Shell\runas -v "HasLUAShield" -d "" -f >nul
reg add HKEY_CLASSES_ROOT\Thonny.py\Shell\runas\command -ve -d "\"C:\Users\moshiko\AppData\Local\Microsoft\WindowsApps\python3.10.exe\" \"%%1\"" -f >nul
