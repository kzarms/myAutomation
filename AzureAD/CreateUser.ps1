<#
[CmdletBinding()]

Param(
    [Parameter(Mandatory=$False)]
    [string]$FirstName = "Alise",
    [string]$LastName = "Johnson",
    [string]$JobTitle = "",
    [string]$UserType = "",
    [string]$Manager = "",
    [string]$Department = "",
    [string]$ExpireDate = "",
    [string]$Pass = "Zooplus1999!",
    [string]$OfficeLocation = "",
    [switch]$TestMode
    )
#>
$TestMode = 0
if($TestMode){
    Write-Output "Test mode"
    Write-Output ("Name is: " + $FirstName + " " + $LastName)
    Pause
    Exit
}
#Code execution
