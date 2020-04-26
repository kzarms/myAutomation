
$scriptRoot  = Split-Path -Parent $MyInvocation.MyCommand.Path
. $scriptRoot\CreateUser.ps1 

#region tests
Describe "Basic user Display name and Mail address tests" {
    Context "Test CreateUserDisplayName function" {
        It "DisplayName basig generation" {
            CreateUserDisplayName -FirstName "Alice" -LastName "Boris" | Should -Be "Alice Boris (External RAS/VDI)"
        }
        It "DisplayName with spaces" { 
            CreateUserDisplayName -FirstName " Alice" -LastName " Boris " | Should -Be "Alice Boris (External RAS/VDI)"
            }
        It "DisplayName with spaces in between" { 
            CreateUserDisplayName -FirstName " Alice" -LastName " Boris Jonson" | Should -Be "Alice Boris Jonson (External RAS/VDI)"
            } 
        It "DisplayName with special charts" {
            CreateUserDisplayName -FirstName "Alice " -LastName "Böris" | Should -Be "Alice Böris (External RAS/VDI)"
            }
        It "Fail test Wrong creation" {
            CreateUserDisplayName -FirstName "Alice " -LastName "Böris" | Should -Not -Be "Alice Boris (External RAS/VDI)"
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
            CreateUserMailExt -FirstName "Alice" -LastName " Boris Jonson" | Should -Be "alice.borisjonson_ext"
            }
        It "Mail address with special cahrs" {
            CreateUserMailExt -FirstName "Alice" -LastName "Böris" | Should -Be "alice.boris_ext"
            }
        It "Fail Mail address with apper cahrs" {
            CreateUserMailExt -FirstName "Alice" -LastName "Boris" | Should -Not -BeExactly "alice.Boris_ext"
            }
      }
}

#end region
