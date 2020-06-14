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
variable "lpass" {
  description = "Linux Admin Password"
}
#Defined locations
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