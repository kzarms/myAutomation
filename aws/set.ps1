$sshFile="TFSetup.pem"
$ip = "3.120.247.206"

Start-Process icacls -ArgumentList "/c /t /inheritance:d"
Start-Process icacls -ArgumentList ("/c /t /grant " + $env:USERNAME + ":F")
Start-Process icacls -ArgumentList '/c /t /remove Administrator "Authenticated Users" BUILTIN\Administrators BUILTIN Everyone System Users'

ssh -i $sshFile ec2-user@$ip