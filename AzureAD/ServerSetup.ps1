Set-TimeZone "W. Europe Standard Time"

Get-NetAdapter


Rename-Computer -ComputerName $ComputerName

#Enable RDP
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

Get-TimeZone