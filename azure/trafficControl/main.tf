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
  service_name  = "TrafficControl"
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
#Create a routing table
resource "azurerm_route_table" "publictable" {
  name                          = "publictable"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  disable_bgp_route_propagation = false

  tags = local.tags
}
resource "azurerm_route" "prod_route" {
  name                    = "productionsubnet"
  resource_group_name     = azurerm_resource_group.rg.name
  route_table_name        = azurerm_route_table.publictable.name
  address_prefix          = "10.0.1.0/24"
  next_hop_type           = "VirtualAppliance"
  next_hop_in_ip_address  = "10.0.2.4"
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
resource "azurerm_subnet" "sb_pub" {
  name                 = "Public"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vNet.name
  address_prefix        = "10.0.0.0/24"
}
resource "azurerm_subnet" "sb_int" {
  name                 = "Internal"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vNet.name
  address_prefix       = "10.0.1.0/24"
}
resource "azurerm_subnet" "sb_dmz" {
  name                 = "DMZ"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vNet.name
  address_prefix       = "10.0.2.0/24"
}
#Assign public subnet custom route
resource "azurerm_subnet_route_table_association" "example" {
  subnet_id      = azurerm_subnet.sb_pub.id
  route_table_id = azurerm_route_table.publictable.id
}

#VM creation based on myNumber
#Network interface
resource "azurerm_network_interface" "nvaInt" {
  name                  = "nvaInt"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location
  enable_ip_forwarding  = true

  ip_configuration {
    name                          = "config"
    subnet_id                     = azurerm_subnet.sb_int.id
    private_ip_address_allocation = "dynamic"
  }
}
resource "azurerm_network_interface" "nvaDMZ" {
  name                  = "nvaDMZ"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location
  enable_ip_forwarding  = true

  ip_configuration {
    name                          = "config"
    subnet_id                     = azurerm_subnet.sb_dmz.id
    private_ip_address_allocation = "dynamic"
  }
}
#VM creation
resource "azurerm_linux_virtual_machine" "nwa" {
  name                  = "nva"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location
  network_interface_ids = [
    azurerm_network_interface.nvaInt.id,
    azurerm_network_interface.nvaDMZ.id
  ]
  size                            = "Standard_D2s_v3"

  admin_username                  = local.luser
  admin_password                  = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "nwa-disk"
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

#Test VMs for check
resource "azurerm_public_ip" "PubIp" {
  name                    = "PubIp"
  resource_group_name     = azurerm_resource_group.rg.name
  location                = azurerm_resource_group.rg.location
  allocation_method       = "Dynamic"
  idle_timeout_in_minutes = 30

  tags = local.tags
}
resource "azurerm_network_interface" "vm1net" {
  name                  = "vm1net"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location

  ip_configuration {
    name                          = "config"
    subnet_id                     = azurerm_subnet.sb_pub.id
    private_ip_address_allocation = "dynamic"
    public_ip_address_id          = azurerm_public_ip.PubIp.id
  }
}
resource "azurerm_network_interface" "vm2net" {
  name                  = "vm2net"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location

  ip_configuration {
    name                          = "config"
    subnet_id                     = azurerm_subnet.sb_int.id
    private_ip_address_allocation = "dynamic"
  }
}
resource "azurerm_linux_virtual_machine" "vm1" {
  name                  = "vm1"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location
  network_interface_ids = [azurerm_network_interface.vm1net.id]
  size                            = "Standard_D2s_v3"

  admin_username                  = local.luser
  admin_password                  = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "vm1-disk"
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
  # Test post deployment actions after creation
#  provisioner "remote-exec" {
#    connection {
#      type     = "ssh"
#      host     = azurerm_public_ip.PubIp.ip_address
#      user     = local.luser
#      password = var.lpass
#    }

#    inline = [
#      "ping -c 4 8.8.8.8 > ping.txt",
#      "cat ping.txt"
#    ]
#  }
}
resource "azurerm_linux_virtual_machine" "vm2" {
  name                  = "vm2"
  resource_group_name   = azurerm_resource_group.rg.name
  location              = azurerm_resource_group.rg.location
  network_interface_ids = [azurerm_network_interface.vm2net.id]
  size                            = "Standard_D2s_v3"

  admin_username                  = local.luser
  admin_password                  = var.lpass
  disable_password_authentication = false

  os_disk {
    name                 = "vm2-disk"
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
#Output
output "VmIP" {
  value       = "ssh -o \"StrictHostKeyChecking no\" ${local.luser}@${azurerm_public_ip.PubIp.ip_address}"
  description = "The Virtual Machine IP"
}