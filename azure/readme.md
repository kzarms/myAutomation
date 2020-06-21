# My code and samples for Azure
Preparation for Azure Architect certification examp

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
ansible-playbook test.yml
ansible all --user useradmin -k -m ping -i ./myazure_rm.yml
```