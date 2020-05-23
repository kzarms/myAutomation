#Main body file
#Vars to connect to the cloud
variable "subscription_id" {
  description = "Subscribtion id for Azure"
}
variable "client_id" {
  description = "Client ID in the AzureAD"
}
variable "client_secret" {
  description = "Client passwords in the AzureAD"
}
variable "tenant_id" {
  description = "Tenant ID"
}
#Vars for solution
resource "random_integer" "suffix" {
  min = 1000
  max = 9999
}
variable "solution" {
  default = "MySolution"
  description = "The name of the solution"
}
variable "location" {
  default = "westeurope"
  description = "The location of the resources"
}
variable "tags" {
    description = "Tags assigned to the resources"
    default = {
        dept    ="its"
        env     ="prod"
        owner   ="its-dm"
        tier    ="low"
        service ="MeetingConcierge"
    }
}

provider "azurerm" {
  version = "=2.0.0"

  features {}

  #Connection to the Azure RM
  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  tenant_id       = var.tenant_id
}

#Resources
resource "azurerm_resource_group" "rg" {
  name     = "${var.solution}${random_integer.suffix.result}"
  location = var.location
  tags = var.tags
}

resource "azurerm_storage_account" "storage" {
  name                     = "${lower(var.solution)}${random_integer.suffix.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"

  tags = var.tags
}

resource "azurerm_storage_table" "meetings" {
  name                 = "meetings"
  storage_account_name = azurerm_storage_account.storage.name
}
resource "azurerm_storage_table" "roomlist" {
  name                 = "roomlist"
  storage_account_name = azurerm_storage_account.storage.name
}

#Output
output "Name" {
  value       = azurerm_resource_group.rg.name
  description = "The hostname of the website"
}

output "pkey" {
  value       = azurerm_storage_account.storage.primary_access_key
  description = "The hostname of the website"
}