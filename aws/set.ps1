$sshFile="TFSetup.pem"
$ip = "3.120.247.206"

Start-Process icacls -ArgumentList "/c /t /inheritance:d"
Start-Process icacls -ArgumentList ("/c /t /grant " + $env:USERNAME + ":F")
Start-Process icacls -ArgumentList '/c /t /remove Administrator "Authenticated Users" BUILTIN\Administrators BUILTIN Everyone System Users'

ssh -i $sshFile ec2-user@$ip

#Check MS Graph
Install-Module Microsoft.Graph
Connect-Graph
Get-MgUser | select -First 5

$FirstName = "Alex"
$LastName = "Fox"
$PasswordProfile = New-Object -TypeName Microsoft.Graph.Model.PasswordProfile
Microsoft.Open.AzureAD.Model.PasswordProfile
$PasswordProfile.Password = "P@ssw0rd!"

New-MgUser `
    -GivenName $FirstName `
    -Surname $LastName `
    -DisplayName ($FirstName + " " + $LastName) `
    -Password "P@sswotrf!"

###
ansible -i inv.yaml --user ec2-user --private-key TFSetup.pem --module-name ping all

Ansible-lint
https://www.ansible.com/blog/ansible-linting-with-github-actions
