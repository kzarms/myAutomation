Import-Module AZ

Connect-AzAccount

# Get-AzLocation | sort DisplayName | ft *
# Get-AzVMSize -Location "germanywestcentral" | Sort-Object Name | Format-Table *

$TFDisplayName = "Terraform SP Account"
$Result = Get-AzADServicePrincipal -DisplayName $TFDisplayName

if($null -eq $Result){
    #Create a SP for tf
    $Pass = ([System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes((New-Guid)))).substring(0,16)
    $credentials = New-Object Microsoft.Azure.Commands.ActiveDirectory.PSADPasswordCredential `
        -Property @{
            StartDate=Get-Date;
            EndDate=Get-Date -Year 2024;
            Password=$Pass
        }

    $sp = New-AzAdServicePrincipal `
        -DisplayName $TFDisplayName `
        -PasswordCredential $credentials

    New-AzRoleAssignment `
        -ApplicationId ($sp.ApplicationId.Guid) `
        -RoleDefinitionName "Contributor"

    $subscription_id = (Get-AzSubscription).Id
    $client_id = $sp.ApplicationId.Guid
    $client_secret = $Pass
    $tenant_id = (Get-AzContext).Tenant.Id

    Write-Output $subscription_id
    Write-Output $client_id
    Write-Output $client_secret
    Write-Output $tenant_id
    #Vrite to the file
    $FileName = "./terraform.tfvars"
    Add-Content $FileName ('subscription_id = "' + $subscription_id + '"')
    Add-Content $FileName ('client_id       = "' + $client_id + '"')
    Add-Content $FileName ('client_secret   = "' + $client_secret + '"')
    Add-Content $FileName ('tenant_id       = "' + $tenant_id + '"')
} else {
    Write-Output "The account $TFDisplayName exists"
}
