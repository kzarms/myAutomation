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
#
Param(
[Parameter(Mandatory=$False)]
   [string]$FirstName = "",
   [string]$LastName = "",   
   [string]$JobTitle = "",
   [string]$UserType = "",
   [string]$Manager = "",
   [string]$Department = "",
   [string]$ExpireDate = "",
   [string]$Pass = "Zooplus1999!",
   [string]$OfficeLocation = ""
)
#>
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
    return $Result
}
function CheckADUser($UserName){
    #Return Azure Uuser object if user exists and 0 if not
    return 0
}
#endregion
#region tests
Describe 'Basic Pester Tests' {
    Context 'Test CreateUserDisplayName function' {
        It 'OK' { CreateUserDisplayName -FirstName "Alice" -LastName "Boris" | Should -Be "Alice Boris (External RAS/VDI)" }
        It 'OK' { CreateUserDisplayName -FirstName " Alice" -LastName " Boris " | Should -Be "Alice Boris (External RAS/VDI)" } 
        It 'OK' { CreateUserDisplayName -FirstName "Alice " -LastName "Böris" | Should -Be "Alice Böris (External RAS/VDI)" }
        It 'Fail' { CreateUserDisplayName -FirstName "Alice " -LastName "Böris" | Should -Not -Be "Alice Boris (External RAS/VDI)" }  
      }
      Context 'Test CreateUserMailExt function' {
        #Can not cher for different cases   
        It 'OK' { CreateUserMailExt -FirstName "Alice" -LastName "Boris" | Should -Be "alice.boris_ext" }
        It 'OK' { CreateUserMailExt -FirstName "Alice" -LastName "Böris" | Should -Be "alice.boris_ext" }
        It 'Fail' { CreateUserMailExt -FirstName "Alice" -LastName "Boris" | Should -Not -Be "alice.böris_ext" }
      }
}
#end region