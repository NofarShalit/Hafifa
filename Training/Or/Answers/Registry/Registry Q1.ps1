$REG_PATH = ""
$FIRST_WORD = $true
$USER_INPUT = Read-Host -Prompt "Enter the Registry path to check"
$USER_INPUT = $USER_INPUT.Split("\\")
foreach ($WORD in $USER_INPUT) 
{
    if (($WORD -eq "COMPUTER") -and ($FIRST_WORD -eq $true))
    { continue }
    
    if ($WORD -eq "HKEY_CLASSES_ROOT")
    { $REG_PATH = ("{0}\{1}" -f $REG_PATH,"HKCR:") }
    elseif ($WORD -eq "HKEY_CURRENT_USER")
    { $REG_PATH = ("{0}\{1}" -f $REG_PATH,"HKCU:") }
    elseif ($WORD -eq "HKEY_LOCAL_MACHINE")
    { $REG_PATH = ("{0}\{1}" -f $REG_PATH,"HKLM:") }
    elseif ($WORD -eq "HKEY_USERS")
    { $REG_PATH = ("{0}\{1}" -f $REG_PATH,"HKU:") }
    elseif ($WORD -eq "HKEY_CURRENT_CONFIG")
    { $REG_PATH = ("{0}\{1}" -f $REG_PATH,"HKCC:") }
    else
    { $REG_PATH = ("{0}\{1}" -f $REG_PATH,$WORD) }
    $FIRST_WORD = $false
}
$REG_PATH = $REG_PATH.Remove(0,1)
Get-ChildItem -path $REG_PATH -Recurse -ErrorAction SilentlyContinue | Where-Object LastWriteTime -gt (get-date).AddDays(-1) | sort LastWriteTime