# Configure the Microsoft Azure Provider
provider "azurerm" {
  # We recommend pinning to the specific version of the Azure Provider you're using
  # since new versions are released frequently
  version = "=2.0.0"

  features {}

  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  tenant_id       = var.tenant_id
}
#
#Generate a random number
resource "random_integer" "suffix" {
  min = 1000
  max = 9999
}
#Variables
locals {
  service_name  = "vmManagment"
  #location = "germanywestcentral"
  location = "westeurope"
  owner = "Konstantin"
  luser = "useradmin"
  myNumber = 3
  #
  tags = {
    env           = "dev"
    tier          = "research"
    SLA           = "24"
    costcenter    = "12345"
  }
}
# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = "${local.service_name}${random_integer.suffix.result}"
  location = local.location
  tags = merge(local.tags, {Name = local.service_name, Owner = local.owner})
}
#Create first vNet
resource "azurerm_virtual_network" "vNet" {
  name                = "vNet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  address_space       = ["10.0.0.0/16"]
  dns_servers         = ["10.0.0.4", "8.8.8.8"]

  tags = local.tags
}
#Attach subnet to the vNet
resource "azurerm_subnet" "subnet" {
  name                 = "Internal"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vNet.name
  address_prefix        = "10.0.0.0/24"
}
#VM creation based on myNumber
#Create public IP
resource "azurerm_public_ip" "PubIp" {
  name                    = "vm1-pubIp"
  resource_group_name     = azurerm_resource_group.rg.name
  location                = azurerm_resource_group.rg.location
  allocation_method       = "Dynamic"
  idle_timeout_in_minutes = 30

  tags = local.tags
}
#Network interface
resource "azurerm_network_interface" "vm1net" {
  name                  = "vm1-net"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location

  ip_configuration {
    name                          = "config"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Static"
    private_ip_address            = "10.0.0.4"
    public_ip_address_id          = azurerm_public_ip.PubIp.id
  }
}
#VM windows
resource "azurerm_windows_virtual_machine" "vm1" {
  name                = "vm1"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  size                = "Standard_D2s_v3"
  computer_name       = "adds"
  admin_username      = local.luser
  admin_password      = var.lpass
  timezone            = "W. Europe Standard Time"

  network_interface_ids = [
    azurerm_network_interface.vm1net.id,
  ]

  os_disk {
    name                 = "vm1-disk"
    caching              = "None"
    storage_account_type = "StandardSSD_LRS"
  }

  source_image_reference {
    publisher = "MicrosoftWindowsServer"
    offer     = "WindowsServer"
    sku       = "2019-Datacenter"
    version   = "latest"
  }
}
#Disable firewall
resource "azurerm_virtual_machine_extension" "fwdisable" {
  name                 = "fwdisable"
  virtual_machine_id   = azurerm_windows_virtual_machine.vm1.id
  publisher            = "Microsoft.Compute"
  type                 = "CustomScriptExtension"
  type_handler_version = "1.9"
  settings = <<SETTINGS
  {
    "commandToExecute": "powershell.exe -Command \"Get-NetFirewallProfile | Set-NetFirewallProfile -Enabled False\""
  }
SETTINGS
}
#Output
data "azurerm_public_ip" "example" {
  name                = azurerm_public_ip.PubIp.name
  resource_group_name = azurerm_windows_virtual_machine.vm1.resource_group_name
}
output "rdp" {
  value = "mstsc /v:${data.azurerm_public_ip.example.ip_address}"
}
output "ps-session" {
  value = "New-PSSession -ComputerName ${data.azurerm_public_ip.example.ip_address}"
}
