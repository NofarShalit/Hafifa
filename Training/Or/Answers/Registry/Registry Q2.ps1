$REGISTRY_PATH = "HKLM:\SOFTWARE\Policies\Microsoft\Windows"
$VALUE_NAME = "LockScreenImage"
$VALUE = Read-Host -Prompt "Enter the image path"
if (-Not (Test-Path "$REGISTRY_PATH\Personalization"))
{ New-Item -Path $REGISTRY_PATH -Name "Personalization" }
New-ItemProperty -Path "$REGISTRY_PATH\Personalization" -Name $VALUE_NAME -Value $VALUE -PropertyType "REG_SZ"