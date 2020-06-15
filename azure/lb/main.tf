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
  service_name  = "lb"
  location = "germanywestcentral"
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

  tags = local.tags
}
#Attach subnet to the vNet
resource "azurerm_subnet" "sb" {
  name                 = "Internal"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vNet.name
  address_prefix     = "10.0.0.0/24"
}
#Create public IP
resource "azurerm_public_ip" "PubIp" {
  name                    = "PubIp"
  resource_group_name     = azurerm_resource_group.rg.name
  location                = azurerm_resource_group.rg.location
  allocation_method       = "Dynamic"
  idle_timeout_in_minutes = 30

  tags = local.tags
}
#Create load balancer
resource "azurerm_lb" "lb" {
  name                = "LoadBalancer"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  frontend_ip_configuration {
    name                 = "PublicIPAddress"
    public_ip_address_id = azurerm_public_ip.PubIp.id
  }
}
resource "azurerm_lb_backend_address_pool" "pool" {
  resource_group_name = azurerm_resource_group.rg.name
  loadbalancer_id     = azurerm_lb.lb.id
  name                = "BackEndAddressPool"
}
#VM creation based on myNumber
#Network interface
resource "azurerm_network_interface" "lan" {
  count               = local.myNumber
  name                = "acctni${count.index}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

 ip_configuration {
   name                          = "config"
   subnet_id                     = azurerm_subnet.sb.id
   private_ip_address_allocation = "dynamic"
 }
}
resource "azurerm_linux_virtual_machine" "vm" {
  count                 = local.myNumber
  name                  = "vm${count.index}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  network_interface_ids = [element(azurerm_network_interface.lan.*.id, count.index)]
  size               = "Standard_D2s_v3"

  admin_username      = local.luser
  admin_password = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "vm${count.index}-os-disk"
    caching              = "None"
    storage_account_type = "StandardSSD_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

 tags = local.tags
}
resource "azurerm_lb_probe" "sshCheck" {
  resource_group_name = azurerm_resource_group.rg.name
  loadbalancer_id     = azurerm_lb.lb.id
  name                = "ssh-running-probe"
  port                = 22
}
resource "azurerm_lb_rule" "ssh" {
  resource_group_name            = azurerm_resource_group.rg.name
  loadbalancer_id                = azurerm_lb.lb.id
  name                           = "ssh"
  protocol                       = "Tcp"
  frontend_port                  = 22
  backend_port                   = 22
  backend_address_pool_id        = azurerm_lb_backend_address_pool.pool.id
  frontend_ip_configuration_name = "PublicIPAddress"
  probe_id                       = azurerm_lb_probe.sshCheck.id

  load_distribution              = "SourceIP"
}
resource "azurerm_network_interface_backend_address_pool_association" "test" {
  count = local.myNumber
  network_interface_id    = azurerm_network_interface.lan[count.index].id
  ip_configuration_name   = "config"
  backend_address_pool_id = azurerm_lb_backend_address_pool.pool.id
}
#
output "IP" {
  value       = azurerm_public_ip.PubIp.ip_address
  description = "The Public IP"
}