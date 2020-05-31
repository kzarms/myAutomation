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
  default = "LabMeetingConcierge"
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
#Connection to the Azure RM
provider "azurerm" {
  version = "=2.0.0"

  features {}

  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  tenant_id       = var.tenant_id
}
#Resources, create a RG as MeetingConciergeXXXX
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
resource "azurerm_logic_app_workflow" "RoomBooking" {
  name                = "Room1-Booking"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}
resource "azurerm_logic_app_trigger_custom" "example" {
  name         = "NewEvent"
  logic_app_id = azurerm_logic_app_workflow.RoomBooking.id

  body = <<BODY
  {
    "recurrence": {
      "frequency": "Minute",
      "interval": 3,
      "timeZone": "W. Europe Standard Time"
    },
    "splitOn": "@triggerBody()?['value']",
    "type": "ApiConnection",
    "inputs": {
      "host": {
        "connection": {
          "name": "@parameters('$connections')['Replaceoffice365Replace']['connectionId']"
        }
      },
      "method": "get",
      "path": "/datasets/calendars/v3/tables/@{encodeURIComponent(encodeURIComponent('AAMkAGRmYjNlNjA3LWU4YTgtNDI2OS1iNTYyLTQ4NjAxMjYxNmU5ZgBGAAAAAACgJfmJRx6JQ5JluMCgvJexBwCAIU6qd3oET6pgS3LIim63AAAAAAEGAACAIU6qd3oET6pgS3LIim63AADRZzN5AAA='))}/onnewitems"
    },
    "description": "When a new calendar event v3"
  }
  BODY

}
resource "azurerm_logic_app_action_custom" "example" {
  name         = "example-action"
  logic_app_id = azurerm_logic_app_workflow.RoomBooking.id

  body = <<BODY
  {
    "description": "A variable to configure the auto expiration age in days. Configured in negative number. Default is -30 (30 days old).",
    "inputs": {
        "variables": [
            {
                "name": "ExpirationAgeInDays",
                "type": "Integer",
                "value": -30
            }
        ]
    },
    "runAfter": {},
    "type": "InitializeVariable"
  }
  BODY

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