#Vars to connect to the cloud
variable "subscription_id" {
  description = "Subscription ID"
}
variable "client_id" {
  description = "User ID"
}
variable "client_secret" {
  description = "User Password"
}
variable "tenant_id" {
  description = "Tennant ID"
}
#Defined locations
variable "service_name" {
  description = "Service Name"
  default = "myLab"
}
variable "location" {
  default = "westeurope"
  description = "The main location for the solution"
}
variable "tags" {
    default = {
        env           = "dev"
        tier          = "research"
        SLA           = "24"
        costcenter    = "12345"
    }
}