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
  service_name  = "network"
  owner = "Konstantin"
  luser = "useradmin"
}
# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = "${local.service_name}${random_integer.suffix.result}"
  location = var.location
  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
}
#Define main network settings
resource "azurerm_network_security_group" "defaultSG" {
  name                = "defaultSG"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
}
#Create a netwrok with subnets
resource "azurerm_virtual_network" "vNet" {
  name                = "Azure-vNet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  address_space       = ["10.0.0.0/16"]
  #dns_servers         = ["10.0.0.4", "10.0.0.5"]

  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
}
resource "azurerm_subnet" "int" {
  name                 = "Internal"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vNet.name
  address_prefix     = "10.0.0.0/24"
}
resource "azurerm_subnet" "ext" {
  name                 = "External"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vNet.name
  address_prefix     = "10.0.1.0/24"

  #network_security_group_id = azurerm_network_security_group.defaultSG.id
}
resource "azurerm_subnet" "gwsubnet" {
  name                 = "GatewaySubnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vNet.name
  address_prefix       = "10.0.255.0/24"
}
resource "azurerm_local_network_gateway" "onpremise" {
  name                = "onpremise"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  gateway_address     = "2.201.84.150"
  address_space       = ["192.168.178.0/24"]
}
resource "azurerm_public_ip" "gwip" {
  name                = "GWpub"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  allocation_method = "Dynamic"
}
resource "azurerm_virtual_network_gateway" "gw" {
  name                = "GW"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  type     = "Vpn"
  vpn_type = "PolicyBased"

  active_active = false
  enable_bgp    = false
  sku           = "Basic"

  ip_configuration {
    name                          = "vnetGatewayConfig"
    public_ip_address_id          = azurerm_public_ip.gwip.id
    private_ip_address_allocation = "Dynamic"
    subnet_id                     = azurerm_subnet.gwsubnet.id
  }

}
resource "azurerm_virtual_network_gateway_connection" "onpremise" {
  name                = "onpremise"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  type                       = "IPsec"
  virtual_network_gateway_id = azurerm_virtual_network_gateway.gw.id
  local_network_gateway_id   = azurerm_local_network_gateway.onpremise.id

  shared_key = var.sharedkey
}
#Create VM1 for tests
#Request public IP
resource "azurerm_public_ip" "vmip" {
  name                    = "vmip"
  resource_group_name     = azurerm_resource_group.rg.name
  location                = azurerm_resource_group.rg.location
  allocation_method       = "Dynamic"
  idle_timeout_in_minutes = 30

  tags = var.tags
}
#Create a network interface with pub IP
resource "azurerm_network_interface" "vmLan" {
  name                = "${local.service_name}-nic1"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.int.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.vmip.id
  }
}
resource "azurerm_linux_virtual_machine" "vm1" {
  name                = "test-vm1"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  size                = "Standard_F2"
  admin_username      = local.luser
  network_interface_ids = [
    azurerm_network_interface.vmLan.id,
  ]

  admin_password = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "test-vm1-disk"
    caching              = "None"
    storage_account_type = "StandardSSD_LRS"

  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  tags = var.tags
}
#Create VM2 for tests
#Request IP
resource "azurerm_network_interface" "vmLan2" {
  name                = "${local.service_name}-nic2"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.ext.id
    private_ip_address_allocation = "Dynamic"
  }
}
resource "azurerm_linux_virtual_machine" "vm2" {
  name                = "test-vm2"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  size                = "Standard_F2"
  admin_username      = local.luser
  network_interface_ids = [
    azurerm_network_interface.vmLan2.id,
  ]

  admin_password = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "test-vm2-disk"
    caching              = "None"
    storage_account_type = "StandardSSD_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  tags = var.tags
}
#Output
#data "azurerm_public_ip" "gwip" {
#  name                = azurerm_public_ip.gwip.name
#  resource_group_name = azurerm_linux_virtual_machine.vm1.resource_group_name
#}

#output "public_ip_address" {
#  value = data.azurerm_public_ip.gwip.ip_address
#}
output "GwIP" {
  value       = azurerm_public_ip.gwip.ip_address
  description = "The Gateway IP"
}
output "VmIP" {
  value       = azurerm_public_ip.vmip.ip_address
  description = "The Virtual Machine IP"
}