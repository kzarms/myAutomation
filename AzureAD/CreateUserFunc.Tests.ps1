﻿<#
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
#Test cases for CreateUser script
#$scriptRoot  = Split-Path -Parent $MyInvocation.MyCommand.Path
#. $scriptRoot\CreateUser.ps1
#$sut = (Split-Path -Leaf $MyInvocation.MyCommand.Path) -replace '\.Tests\.', '.'
#. $scriptRoot\$sut -FirstName $FirstName -LastName $LastName -TestMode $TestMode
#. $scriptRoot\$sut

BeforeAll {
    # DON'T use $MyInvocation.MyCommand.Path
    . $PSCommandPath.Replace('.Tests.ps1','.ps1')
}
#Module describe
$myDynamicModule = New-Module -Name MyDynamicModule {
    function Get-MgUser {}
    function Get-MgDomain {}
    Export-ModuleMember -Function *
}

# import the dynamic module
$myDynamicModule | Import-Module -Force

#region tests
Describe "Basic user Display name and Mail address tests" {
    Context "Test CreateUserDisplayName function" {
        It "DisplayName basig generation" {
            CreateUserDisplayName -FirstName "Alice" -LastName "Boris" | Should -BeExactly "Alice Boris (External RAS/VDI)"
        }
        It "DisplayName with spaces" {
            CreateUserDisplayName -FirstName " Alice" -LastName " Boris " | Should -BeExactly "Alice Boris (External RAS/VDI)"
            }
        It "DisplayName with spaces in between" {
            CreateUserDisplayName -FirstName " Alice" -LastName " Boris Jonson" | Should -BeExactly "Alice Boris Jonson (External RAS/VDI)"
            }
        It "DisplayName with lower cases" {
            CreateUserDisplayName -FirstName " alice" -LastName "boris" | Should -BeExactly "Alice Boris (External RAS/VDI)"
            }
        It "DisplayName with special charts" {
            CreateUserDisplayName -FirstName "Alice " -LastName "Böris" | Should -BeExactly "Alice Böris (External RAS/VDI)"
            }
        It "Fail test Wrong creation" {
            CreateUserDisplayName -FirstName "Alice " -LastName "Böris" | Should -Not -BeExactly "Alice Boris (External RAS/VDI)"
            }
      }
      Context 'Test CreateUserMailExt function' {
        #Can not cher for different cases
        It "Mail address basic generation" {
            CreateUserMailExt -FirstName "Alice" -LastName "Boris" | Should -BeExactly "alice.boris_ext"
            }
        It "Mail address with spaces" {
            CreateUserMailExt -FirstName "Alice" -LastName " Boris" | Should -BeExactly "alice.boris_ext"
            }
        It "Mail address with spaces in between" {
            CreateUserMailExt -FirstName "Alice" -LastName " Boris Jonson" | Should -BeExactly "alice.borisjonson_ext"
            }
        It "Mail address with special cahrs" {
            CreateUserMailExt -FirstName "Alice" -LastName "Böris" | Should -BeExactly "alice.boris_ext"
            }
        It "Fail Mail address with apper cahrs" {
            CreateUserMailExt -FirstName "Alice" -LastName "Boris" | Should -Not -BeExactly "alice.Boris_ext"
            }
      }
}

Describe "MS Graph functions check" {
    Context "Test CheckDomain function" {
        It "Get proper dev domain" {
            Mock Get-MgDomain {
                [PSCustomObject]@{Id='azure.onmicrosoft.com'},
                [PSCustomObject]@{Id='devzooplus.com'},
                [PSCustomObject]@{Id='devzooplus.onmicrosoft.com'}
                }

            CheckDomain | Should -Be "devzooplus.com"
        }
        It "Get proper dev domain" {
            Mock Get-MgDomain {
                [PSCustomObject]@{Id='azure.onmicrosoft.com'},
                [PSCustomObject]@{Id='devzooplus.com'},
                [PSCustomObject]@{Id='devzooplus.onmicrosoft.com'}
                }

            CheckDomain | Should -Be "devzooplus.com"
        }

        It "Get proper prod domain" {
            Mock Get-MgDomain {
                [PSCustomObject]@{Id='azure.onmicrosoft.com'},
                [PSCustomObject]@{Id='zooplus.com'},
                [PSCustomObject]@{Id='zooplus.onmicrosoft.com'}
                }

            CheckDomain | Should -Be "zooplus.com"
        }

        It "Get none valid setup" {
            Mock Get-MgDomain {
                [PSCustomObject]@{Id='azure.onmicrosoft.com'},
                [PSCustomObject]@{Id='zooplus.com'},
                [PSCustomObject]@{Id='zooplus.net'},
                [PSCustomObject]@{Id='zooplus.onmicrosoft.com'}
                }

            CheckDomain | Should -Be 0
        }
    }
    Context "Test CheckUser function" {
        It "Get user by mail name" {
            Mock Get-MgUser {
                [PSCustomObject]@{UserPrincipalName='test.user@devzooplus.com'}
                }
            #Return User UPN
            (CheckUser -UserName "test.user").UserPrincipalName | Should -Be "test.user@devzooplus.com"
        }
        It "Get user by upn" {
            Mock Get-MgUser {
                [PSCustomObject]@{UserPrincipalName='test.user@devzooplus.com'}
                }
            #Return User UPN
            (CheckUser -UserName "test.user@devzooplus.com").UserPrincipalName | Should -Be "test.user@devzooplus.com"
        }
        It "Get user by Display Name" {
            Mock Get-MgUser {
                [PSCustomObject]@{UserPrincipalName='test.user@devzooplus.com'}
                }
            #Return User UPN
            CheckUser -UserName "Test User" | Should -Be 0
        }
        It "Get 0 rezult" {
            Mock Get-MgUser {}

            CheckUser -UserName "test.user@devzooplus.com" | Should -Be 0
        }
    }
}


        #Mock Get-MgDomain {
        #    [PSCustomObject]@{Id='devzooplus.com'}
        #}
        <#
        Mock Get-MgUser {
            $object =  New-Object psobject -Property @{
                UserPrincipalName = $UPN
            }
            return $object
            #[PSCustomObject]@{UserPrincipalName=$UPN}
        }

        Mock Get-MgDomain { [PSCustomObject]@{UserPrincipalName=$UPN}} -ParameterFilter {$UserName -eq "konstantin.zarudaev@devzooplus.com"}

        It "Find existing user by UPN" {
            Get-MgDomain -UserName "konstantin.zarudaev@devzooplus.com" | Should -Be $UPN
        }
        #>

        <#
        It "Find existing user by UPN" {
            (CheckUser -UserName $UPN).UserPrincipalName | Should -Be $UPN
        }
        It "Find existing user by mail" {
            (CheckUser -UserName $UserMailNicName).UserPrincipalName | Should -Be $UPN
        }
        #>


#end region
