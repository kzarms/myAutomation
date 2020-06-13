Import-Module AZ
Connect-AzAccount
$VerbosePreference = "Continue"

#Region VPN
# https://docs.microsoft.com/en-us/learn/modules/connect-on-premises-network-with-vpn-gateway/2-connect-on-premises-networks-to-azure-using-site-to-site-vpn-gateways

$ServiceName = "PrepFor303_"
$Location = "westeurope"
$RandomID = (Get-Random -Minimum 1111 -Maximum 9999).ToString()
$ResourceGroupName = $ServiceName + $RandomID

#Create a RGS for the new Network
$Result = Get-AzResourceGroup -Name $ResourceGroupName -Location $Location -ErrorAction SilentlyContinue
if($Result){
    Write-Verbose "RG $ResourceGroupName exists"
} else {
    #Create a new RG
    New-AzResourceGroup -Name $ResourceGroupName -Location $Location
}

$virtualNetwork = New-AzVirtualNetwork `
  -ResourceGroupName $ResourceGroupName `
  -Location $Location `
  -Name ($ServiceName + "Vnet")`
  -AddressPrefix 10.100.0.0/16

$virtualNetwork

$subnetConfig = Add-AzVirtualNetworkSubnetConfig `
  -Name "default" `
  -AddressPrefix 10.100.0.0/24 `
  -VirtualNetwork $virtualNetwork
$subnetConfig

$virtualNetwork | Set-AzVirtualNetwork
#Get public IP for the GW
$ngwpip = New-AzPublicIpAddress `
    -Name ($ServiceName + "PubIP") `
    -ResourceGroupName $ResourceGroupName `
    -Location $Location `
    -AllocationMethod Static

$subnet = Add-AzVirtualNetworkSubnetConfig `
    -name "GWsubnet2" `
    -AddressPrefix "10.100.250.0/24" `
    -VirtualNetwork $virtualNetwork
#Save config to the net
#$virtualNetwork | Set-AzVirtualNetwork

$ngwIpConfig = New-AzVirtualNetworkGatewayIpConfig `
    -Name ngwipconfig `
    -SubnetId $subnet.Id `
    -PublicIpAddressId $ngwpip.Id

New-AzVirtualNetworkGateway `
    -Name myNGW `
    -ResourceGroupName $ResourceGroupName `
    -Location $Location `
    -IpConfigurations $ngwIpConfig `
    -GatewayType "Vpn" `
    -VpnType "RouteBased" `
    -GatewaySku "Basic" `
    -CustomRoute "192.168.0.0/16"

#End region

New-AzResourceGroup -Location "UK West" -Name "vnet-gateway"
$GwSubnet = New-AzVirtualNetworkSubnetConfig -Name 'gatewaysubnet' -AddressPrefix '10.254.0.0/27'

$ngwpip = New-AzPublicIpAddress `
    -Name "GwPubIP" `
    -ResourceGroupName $ResourceGroupName `
    -Location $Location `
    -AllocationMethod Dynamic

$vnet = New-AzVirtualNetwork `
    -Name "vNet" `
    -AddressPrefix "10.0.0.0/8" `
    -ResourceGroupName $ResourceGroupName `
    -Location $Location `
    -Subnet $GwSubnet

#Find an ID of the new subnet
$GwSubnet = Get-AzVirtualNetworkSubnetConfig -name 'gatewaysubnet' -VirtualNetwork $vnet

#Prepare config
$ngwipconfig = New-AzVirtualNetworkGatewayIpConfig `
    -Name "ngwipconfig" `
    -SubnetId $GwSubnet.Id `
    -PublicIpAddressId $ngwpip.Id

#Create an VPN GW
New-AzVirtualNetworkGateway `
    -Name "myVpnGW" `
    -ResourceGroupName $ResourceGroupName `
    -Location $Location `
    -IpConfigurations $ngwIpConfig `
    -GatewayType "Vpn" `
    -VpnType "RouteBased" `
    -GatewaySku "Basic" `
    -CustomRoute "192.168.178.0/24"

