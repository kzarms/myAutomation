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
  #dns_servers         = ["10.0.0.4", "10.0.0.5"]

  subnet {
    name           = "SalesVNet"
    address_prefix = "10.1.1.0/24"
  }

  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
}
#Create second vNet
resource "azurerm_virtual_network" "MarketingVNet" {
  name                = "MarketingVNet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  address_space       = ["10.2.0.0/16"]
  #dns_servers         = ["10.0.0.4", "10.0.0.5"]

  subnet {
    name           = "SalesVNet"
    address_prefix = "10.2.1.0/24"
  }

  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
}
#Create third vNet in different location (northeurope)
resource "azurerm_virtual_network" "ResearchVNet" {
  name                = "ResearchVNet"
  resource_group_name = azurerm_resource_group.rg.name
  location            = "northeurope"
  address_space       = ["10.3.0.0/16"]
  #dns_servers         = ["10.0.0.4", "10.0.0.5"]

  subnet {
    name           = "ResearchVNet"
    address_prefix = "10.3.1.0/24"
  }

  tags = merge(var.tags, {Name = local.service_name, Owner = local.owner})
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