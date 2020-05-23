#Vars to connect to the cloud
variable "access_key" {
  description = "Access key to connect to the AWS"
}
variable "secret_key" {
  description = "Access key secret to connect to the AWS"
}

provider "aws" {
  version = "~> 2.0"
  region  = "eu-central-1"
  access_key = var.access_key
  secret_key = var.secret_key
}


#Creation
# Create a VPC
resource "aws_vpc" "mainVPC" {
  cidr_block = "192.168.192.0/20"
  enable_dns_hostnames = true

  tags = {
    Dept    ="its"
    Env     ="dev"
    Owner   ="its-dm"
    Tier    ="low"
    Service ="IDSync"
    Name    ="TF Setup VPC"
  }
}
resource "aws_internet_gateway" "default" {
  vpc_id = aws_vpc.mainVPC.id

  tags = {
    Dept    ="its"
    Env     ="dev"
    Owner   ="its-dm"
    Tier    ="low"
    Service ="IDSync"
    Name    ="TF Setup GW"
  }
}
resource "aws_route" "internet_access" {
  route_table_id         = aws_vpc.mainVPC.main_route_table_id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.default.id
}
resource "aws_subnet" "vm_subnet" {
  vpc_id            = aws_vpc.mainVPC.id
  cidr_block        = "192.168.192.0/24"
  availability_zone = "eu-central-1a"
  map_public_ip_on_launch = true

  tags = {
    Dept    ="its"
    Env     ="dev"
    Owner   ="its-dm"
    Tier    ="low"
    Service ="IDSync"
    Name    ="TF Setup Subnet"
  }
}
resource "aws_security_group" "default" {
  name        = "TF Setup SG"
  description = "Used in the terraform"
  vpc_id      = aws_vpc.mainVPC.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  # SSH access from anywhere
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  # outbound internet access
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
resource "aws_instance" "vm1" {
  ami           = "ami-076431be05aaf8080"
  instance_type = "t2.micro"
  key_name = "TF Setup"

  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  subnet_id = aws_subnet.vm_subnet.id

  tags = {
    Dept    ="its"
    Env     ="dev"
    Owner   ="its-dm"
    Tier    ="low"
    Service ="IDSync"
    Name    ="Vm1"
  }
  connection {
    type = "ssh"
    user = "ec2-user"
    host = self.public_ip
    private_key = file("${path.module}/TFSetup.pem")

    # The connection will use the local SSH agent for authentication.
  }
  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y"
    ]
  }
}

#Output
output "MainVPCid" {
  value       = aws_vpc.mainVPC.id
  description = "The VPC ID"
}
output "VmIP" {
  value       = aws_instance.vm1.public_ip
  description = "The VM IP"
}