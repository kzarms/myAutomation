# My code and samples for Ubuntu
Prep

## Terraform
Code example for terraform files

Init, plan, apply and destroy after.
```
terraform init
terraform plan
terraform apply -auto-approve

terraform destroy
```

## Ansible
Code example for ansible files

Simple one time execution
```
ansible-playbook -i 192.168.178.59, ubuntu/ansible/ping.yml
ansible-playbook ubuntu/ansible/ping.yml

#ansible --user kot -k -m ping -i 192.168.178.59

```