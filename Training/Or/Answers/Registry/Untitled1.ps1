$startDate = (get-date).AddDays(-1)
$slogonevents = Get-Eventlog -LogName Security -ComputerName 'DESKTOP-5SB24U6' -after $startDate | where {$_.eventID -eq 4624 }

# Crawl through events; print all logon history with type, date/time, status, account name, computer and IP address if user logged on remotely

foreach ($e in $slogonevents){
    # Logon Successful Events
    # Local (Logon Type 2)
    if (($e.EventID -eq 4624 ) -and ($e.ReplacementStrings[8] -eq 2 -or $e.ReplacementStrings[8] -eq 10)){
        write-host "Type: Logon`tDate: "$e.TimeGenerated "`tStatus: Success`tUser: "$e.ReplacementStrings[5] "`tWorkstation: "$e.ReplacementStrings[11]
    }
}

