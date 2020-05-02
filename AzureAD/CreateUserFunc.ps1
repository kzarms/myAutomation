<#
.DESCRIPTION
The purpose of this script is create a user in Auzre AD with proper values and parameters
To run unit tests you need to instal Pester on our device

    Install-Module Pester -Force -SkipPublisherCheck
    Get-Module Pester -ListAvailable

    if there are module 3 - you need update it with

    Update-Module Pester -Force

.Parameter cmd
    This parameter accept command line execution.
    This example creates an AD user in Azure AD

    .\CreateUser.ps1 -


    Run the tests for the script

    Invoke-Pester ".\CreateUser.ps1"
#>
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
#Import-Module Microsoft.Graph

#region functions
function CreateUserDisplayName($FirstName, $LastName){
    #Create Display name + additional description
    $Result = $FirstName.trim() + " " + $LastName.trim() + " (External RAS/VDI)"
    return $Result
}
function CreateUserMailExt($FirstName, $LastName){
    #The function will take two names and create an ext mail
    $Result = $FirstName.trim() + "." + $LastName.trim() + "_ext"
    #Remove non ASCII symbols and make it lover cases
    $Result = ([Text.Encoding]::ASCII.GetString([Text.Encoding]::GetEncoding("Cyrillic").GetBytes($Result))).ToLower()
    #Remove spaces in between for complex LastNames
    $Result = $Result -replace " ",""
    return $Result
}
function CheckDomain(){
    $Domains = Get-MgDomain | Where-Object {$_.id -notlike "*.onmicrosoft.com"}
    if($Domains.count -eq 1){
        return $Domains[0].Id
    } else {
        return 0
    }
}
function CheckUser($UserName){
    #Return Azure Uuser object if user exists and 0 if not
    if($UserName.contains(" ")){
        #This is a display name
        return 0
    } elseif($UserName.contains("@")){
        #This is a upn
        $Result = Get-MgUser -UserId $UserName -ErrorAction SilentlyContinue
    } else {
        #Not spaces and no @ symbol -> part of the name, get $Domain from Global and create UPN
        $UserName = $UserName + "@" + $Domain
        $Result = Get-MgUser -UserId $UserName -ErrorAction SilentlyContinue
    }

    if($Result.count -eq 1){
        return $Result
    }
    return 0
}


#endregion
#region execution
#Create user upn and email

<#Connect to the MS graph

Invoke-Pester -Script @{Path='.\AzureAD\CreateUser.Tests.ps1';Parameters=@{FirstName='Anna';TestMode='True'}}

$Result = Connect-Graph
if($null -eq $Result){
    Write-Output "No connection to the MS Graph"
    Pause
    Exit
}
#>
<#

#Generate UserName
$UserMailNicName = CreateUserMailExt -FirstName $FirstName -LastName $LastName
$UserUPN = $UserMailNicName + "@" + $Domain
$ManagerUpn = "konstantin.zarudaev"+ "@" + $Domain

$AzureAdUser = CheckUser -UserName $UserUPN
$AzureAdManager = CheckUser -UserName $ManagerUpn

if(!($AzureAdUser)){
    if ($AzureAdManager){
            #If there is manager and no user than create a new user
    $DisplayName = CreateUserDisplayName -FirstName $FirstName -LastName $LastName

    $Result = New-MgUser `
        -DisplayName $DisplayName `
        -AccountEnabled `
        -PasswordProfile @{"Password"=$Pass} `
        -MailNickname $UserMailNicName `
        -UserPrincipalName $UserUPN

    If($Result.count -eq 1){
        Write-Output "User has been created successfully"
    }

    } else {
        Write-Output "Manger is not found"
    }

} else {
    Write-Output "User exists"
}
#endregion
#>
