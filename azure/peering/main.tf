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
  service_name  = "peering"
  owner = "Konstantin"
  luser = "useradmin"
}
# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = "${local.service_name}${random_integer.suffix.result}"
  location = var.location
  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
}
#Create first vNet
resource "azurerm_virtual_network" "SalesVNet" {
  name                = "SalesVNet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  address_space       = ["10.1.0.0/16"]

  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
}
#Create second vNet
resource "azurerm_virtual_network" "MarketingVNet" {
  name                = "MarketingVNet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  address_space       = ["10.2.0.0/16"]

  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
}
#Create third vNet in different location (northeurope)
resource "azurerm_virtual_network" "ResearchVNet" {
  name                = "ResearchVNet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = "northeurope"
  address_space       = ["10.3.0.0/16"]

  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
}
#Attach subnets to the Vnets
resource "azurerm_subnet" "sb1" {
  name                 = "Internal"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.SalesVNet.name
  address_prefix     = "10.1.1.0/24"
}
resource "azurerm_subnet" "sb2" {
  name                 = "Internal"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.MarketingVNet.name
  address_prefix     = "10.2.1.0/24"
}
resource "azurerm_subnet" "sb3" {
  name                 = "Internal"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.ResearchVNet.name
  address_prefix     = "10.3.1.0/24"
}
#Create a local peering between vNet-s in one location
resource "azurerm_virtual_network_peering" "peer1" {
  name                      = "SalesToMarketing"
  resource_group_name       = azurerm_resource_group.rg.name
  virtual_network_name      = azurerm_virtual_network.SalesVNet.name
  remote_virtual_network_id = azurerm_virtual_network.MarketingVNet.id
}

resource "azurerm_virtual_network_peering" "peer2" {
  name                      = "MarketingToSales"
  resource_group_name       = azurerm_resource_group.rg.name
  virtual_network_name      = azurerm_virtual_network.MarketingVNet.name
  remote_virtual_network_id = azurerm_virtual_network.SalesVNet.id
}

#Create global peering between different locations.
resource "azurerm_virtual_network_peering" "gpeer1" {
  name                         = "SalesToResearchVNet"
  resource_group_name          = azurerm_resource_group.rg.name
  virtual_network_name         = azurerm_virtual_network.SalesVNet.name
  remote_virtual_network_id    = azurerm_virtual_network.ResearchVNet.id
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
  #
  allow_gateway_transit = false
}
resource "azurerm_virtual_network_peering" "gpeer2" {
  name                         = "ResearchToSales"
  resource_group_name          = azurerm_resource_group.rg.name
  virtual_network_name         = azurerm_virtual_network.ResearchVNet.name
  remote_virtual_network_id    = azurerm_virtual_network.SalesVNet.id
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true
  #
  allow_gateway_transit = false
}

#Add 3 VMs for tests
#Create 3 network interfaces
resource "azurerm_public_ip" "vmip" {
  name                    = "vmip"
  resource_group_name     = azurerm_resource_group.rg.name
  location                = azurerm_resource_group.rg.location
  allocation_method       = "Dynamic"
  idle_timeout_in_minutes = 30

  tags = var.tags
}
resource "azurerm_network_interface" "vmLan1" {
  name                = "vmLan1"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.sb1.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.vmip.id
  }
}
resource "azurerm_network_interface" "vmLan2" {
  name                = "vmLan2"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.sb2.id
    private_ip_address_allocation = "Dynamic"
  }
}
resource "azurerm_network_interface" "vmLan3" {
  name                = "vmLan3"
  resource_group_name = azurerm_resource_group.rg.name
  location            = "northeurope"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.sb3.id
    private_ip_address_allocation = "Dynamic"
  }
}
#Create 3 VMs
resource "azurerm_linux_virtual_machine" "vm1" {
  name                  = "vm1"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  size                = "Standard_F2"
  admin_username      = local.luser
  network_interface_ids = [ azurerm_network_interface.vmLan1.id ]

  admin_password = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "vm1-disk-1"
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
resource "azurerm_linux_virtual_machine" "vm2" {
  name                  = "vm2"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  size                = "Standard_F2"
  admin_username      = local.luser
  network_interface_ids = [ azurerm_network_interface.vmLan2.id ]

  admin_password = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "vm2-disk-1"
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
resource "azurerm_linux_virtual_machine" "vm3" {
  name                  = "vm3"
  resource_group_name = azurerm_resource_group.rg.name
  location            = "northeurope"
  size                = "Standard_F2"
  admin_username      = local.luser
  network_interface_ids = [ azurerm_network_interface.vmLan3.id ]

  admin_password = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "vm3-disk-1"
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
output "VmIP" {
  value       = azurerm_public_ip.vmip.ip_address
  description = "The Virtual Machine IP"
}