# Parameters
Param (
    [Parameter(Mandatory = $False, HelpMessage = "Specify the path for the file with IP's to be parsed")]
    [string]$IPFilePath = "",
    [Parameter(Mandatory = $False, HelpMessage = "Specify if to run the port scan on the generated DomRec-IPS")]
    [switch]$IPPortScan,
    [Parameter(Mandatory = $False, HelpMessage = "Specify how many port scans to run simultaneously, default is 5")]
    [int]$ConcurrentScans = 5,
    [Parameter(Mandatory = $False, HelpMessage = "Specify if the script should scan the domain for all computer objects")]
    [switch]$ScanDomainComputers
)

# Constants
$IPV4Regex = [regex] "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

# Creating all Folders and Files
if (!(Test-Path "$PSScriptRoot/DomRec")) { New-Item -Path "$PSScriptRoot" -Name "DomRec" -ItemType "directory" }
if (!(Test-Path "$PSScriptRoot/DomRec/Data")) { New-Item -Path "$PSScriptRoot/DomRec" -Name "Data" -ItemType "directory" }
if (!(Test-Path "$PSScriptRoot/DomRec/Scanned Hosts")) { New-Item -Path "$PSScriptRoot/DomRec" -Name "Scanned Hosts" -ItemType "directory" }

# Creating the config file for the unWinter protocol
#if (!(Test-Path "$PSScriptRoot/DomRec/Data/unWinter.txt")) { 
#    $CONFIG = "SkipIPResolver=No"
#    $CONFIG += "SkipIPPortScan=No"
#    New-Item -Path "$PSScriptRoot/DomRec/Data" -Name "unWinter.txt" -ItemType "file" -Value $CONFIG
#}

# Outputting all ip addresses to DomRec-IPS.txt
if ($IPFilePath -ne "") {
    $IPS = (Get-Content -Path $IPFilePath) -split (" ")
    if (Test-Path "$PSScriptRoot/DomRec/Data/DomRec-IPS.txt") { Remove-Item "$PSScriptRoot/DomRec/Data/DomRec-IPS.txt" }
    For ( $i = 0; $i -lt $IPS.length ; $i++ )
    { ((Select-String -InputObject $IPS[$i] -Pattern $IPV4Regex).Matches.groups).Value | Out-File -Append "$PSScriptRoot/DomRec/Data/DomRec-IPS.txt" }
}

# Scanning all IPS
if ($IPPortScan.IsPresent) {
    if (!(Test-Path "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt")) { New-Item -Path "$PSScriptRoot/DomRec/Data" -Name "UnfinishedPortScans.txt" -ItemTye "file" }
    $IPS = (Get-Content -Path "$PSScriptRoot/DomRec/Data/DomRec-IPS.txt") -split ("\n")
    $UnfinishedPortScans = (Get-Content -Path "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt") -split ("\n")

    # Skipping all previously scanned IPs
    $IPCounter = 0
    while (!($UnfinishedPortScans.Contains($IPS[$IPCounter])) -and ($UnfinishedPortScans -ne "")) 
    { $IPCounter++ }

    # Adding IPs until the requested number of concurrent scans reached
    while (($UnfinishedPortScans -split ("\n")).count -lt $ConcurrentScans) { 
        $IPCounter++
        if (!($UnfinishedPortScans.Contains($IPS[$IPCounter])))
        { Out-File -FilePath "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt" -InputObject $IPS[$IPCounter] -Append }
    }
    $IPCounter++
    $UnfinishedPortScans = (Get-Content -Path "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt") -split ("\n")

    # Scanning all UnfinishedIPs
    $UnfinishedPortScansIndex = 0
    while ($UnfinishedPortScans -ne "") {
        if ((Get-Job).count -lt $ConcurrentScans)
        { Start-ThreadJob -Name $UnfinishedPortScans[$UnfinishedPortScansIndex] { ($IP = [string]$input) -and (nmap.exe -A -p- -v --min-rate 10000000 -oN "PSScriptRoot/DomRec/Scanned Hosts/$IP.txt" $IP) } -InputObject $UnfinishedPortScans[$UnfinishedPortScansIndex] }

        else {
            while ((Get-Job).count -eq $ConcurrentScans) { 
                Start-Sleep(10)
                if ((Get-Job -State "Completed").count -gt 0) {
                    $CompletedScanIP = ((Get-Job -State "Completed")[0]).Name
                    Remove-Job -Name $CompletedScanIP
                    Set-Content -Path "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt" -Value (Get-Content -Path "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt" | Select-String -Pattern $CompletedScanIP -NotMatch)
                }
            }
            Start-ThreadJob -Name $IPS[$i] { ($IP = [string]$input) -and (nmap.exe -A -p- -v --min-rate 10000000 -oN "PSScriptRoot/DomRec/Scanned Hosts/$IP.txt" $IP) } -InputObject $IPS[$i]
        }
        $UnfinishedPortScansIndex++
    }

    # Continuing the scan after finishing all UnfinishedIPs
    For ( ; $IPCounter -lt $IPS.length ; $IPCounter++ ) {
        if ((Get-Job).count -lt $ConcurrentScans) {
            Start-ThreadJob -Name $IPS[$i] { ($IP = [string]$input) -and (nmap.exe -A -p- -v --min-rate 10000000 -oN "PSScriptRoot/DomRec/Scanned Hosts/$IP.txt" $IP) } -InputObject $IPS[$i]
            Out-File -FilePath "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt" -InputObject $IPS[$IPCounter] -Append
        }

        else {
            while ((Get-Job).count -eq $ConcurrentScans) { 
                Start-Sleep(10)
                if ((Get-Job -State Completed).count -gt 0) {
                    $CompletedScanIP = ((Get-Job -State Completed)[0]).Name
                    Remove-Job -Name $CompletedScanIP
                    Set-Content -Path "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt" -Value (Get-Content -Path "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt" | Select-String -Pattern $CompletedScanIP -NotMatch)
                }
            }
            
            
            
            Start-ThreadJob -Name $IPS[$i] { ($IP = [string]$input) -and (nmap.exe -A -p- -v --min-rate 10000000 -oN "PSScriptRoot/DomRec/Scanned Hosts/$IP.txt" $IP) } -InputObject $IPS[$i]
            Out-File -FilePath "$PSScriptRoot/DomRec/Data/UnfinishedPortScans.txt" -InputObject $IPS[$IPCounter] -Append
        }        
    }
    # Waiting for the last scans to complete
    Get-Job | Wait-Job
}

if ($ScanDomainComputers.IsPresent)
{
    Import-Module ActiveDirectory



}