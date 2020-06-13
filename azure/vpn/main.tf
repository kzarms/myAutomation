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

# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = "${var.service_name}${random_integer.suffix.result}"
  location = var.location
  tags = merge(var.tags, {Name = "MyLab"})
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

  subnet {
    name           = "mainVMs"
    address_prefix = "10.0.0.0/24"
  }

  subnet {
    name           = "DMZ"
    address_prefix = "10.0.1.0/24"
    security_group = azurerm_network_security_group.defaultSG.id
  }

  tags = var.tags
}

#Define ???
resource "azurerm_virtual_wan" "vWan" {
  name                = "Azure-vWan"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
}
#Define ?1
resource "azurerm_virtual_hub" "vHub" {
  name                = "Azure-vHub"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  virtual_wan_id      = azurerm_virtual_wan.vWan.id
  address_prefix      = "10.0.255.0/24"
}
#Create GW
resource "azurerm_vpn_gateway" "gw" {
  name                = "VpnGw"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  virtual_hub_id      = azurerm_virtual_hub.vHub.id
}