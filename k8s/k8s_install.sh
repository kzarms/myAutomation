#!/usr/bin/bash
# chmod +x k8s_install.sh
# sudo ./k8s_install.sh

dnf install nano vim mc net-tools tcpdump wget curl -y

# Prepare Server for operations
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux

dnf update
dnf upgrade

# Enable NAT
sysctl -w net.ipv4.ip_forward=1
sysctl net.ipv4.ip_forward

firewall-cmd --get-active-zone
nmcli connection modify ens224 connection.zone internal
nmcli connection modify ens192 connection.zone external
firewall-cmd --get-active-zone

firewall-cmd --zone=external --add-masquerade --permanent
firewall-cmd --reload

ssh-keygen -t rsa -b 4096

ssh-copy-id root@node1.local
ssh-copy-id root@node2.local

# Change color
export PS1="\e[0;32m[\u@\h \W]\$ \e[m "


#systemctl enabled firewalld
#systemctl start firewalld

#firewall-cmd --permanent --direct --passthrough ipv4 -t nat -I POSTROUTING -o ens192 -j MASQUERADE -s 192.168.0.0/24
#firewall-cmd --reload

#
#nft add table nat
#nft 'add chain nat postrouting { type nat hook postrouting priority 100 ; }'
#nft add rule nat postrouting ip saddr 192.168.0.0/24 oif ens192 snat 192.168.24.64
#nft add rule nat postrouting masquerade

# Installing process
echo "Simple installating K8S on the node."


# Add Static names for DNS
echo "192.168.0.254 k8smaster.local" | tee -a /etc/hosts
echo "192.168.0.21 node1.local" | tee -a /etc/hosts
echo "192.168.0.22 node2.local" | tee -a /etc/hosts

# Disable SElinux and swap file
# setenforce 0

# sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
# reboot

# Firewall Setup
firewall-cmd --permanent --add-port=6443/tcp --zone=internal
firewall-cmd --permanent --add-port=8080/tcp --zone=external
firewall-cmd --permanent --add-port=2379-2380/tcp --zone=internal
firewall-cmd --permanent --add-port=10250/tcp --zone=internal
firewall-cmd --permanent --add-port=10251/tcp --zone=internal
firewall-cmd --permanent --add-port=10252/tcp --zone=internal
firewall-cmd --permanent --add-port=10255/tcp --zone=internal
firewall-cmd --reload
# disable swap
swapoff -a
sed -i 's/\/dev\/mapper\/cl-swap/\#\/dev\/mapper\/cl-swap/g' /etc/fstab

# Remove 
# dnf remove podman buildah -y

# Add docker repo
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo

# Install docker
dnf install docker-ce -y

# Check
docker --version

# Start service
systemctl enable docker
systemctl start docker

# systemctl status docker

# K8S
# https://kubernetes.io/docs/tasks/tools/install-kubectl/

cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF
#yum install -y kubectl
dnf install kubeadm -y 

'''
cat <<EOF > kubeadm-config.yaml
apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
# kubernetesVersion: 1.18.1                   #<-- Use the word stable for newest version
controlPlaneEndpoint: "centos8.local:6443"  #<-- Use the node alias not the IP
networking:
    podSubnet: 10.10.0.0/16                 #<-- Match the IP range from the Calico config file
EOF
'''

# Init the claster
# kubeadm init --config=kubeadm-config.yaml --upload-certs | tee kubeadm-init.out # Save output for future review
kubeadm init \
--control-plane-endpoint 'k8smaster.local' \
--pod-network-cidr '10.10.0.0/16' \
--service-cidr '10.20.0.0/16' \
--upload-certs | tee kubeadm-init.out

# kubeadm init --control-plane-endpoint 'centos8.local' --pod-network-cidr '10.10.0.0/16' --service-cidr '10.20.0.0/16' --upload-certs | tee kubeadm-init.out
# Exit form sudo mode
# exit

# mkdir -p $HOME/.kube
# sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
# sudo chown $(id -u):$(id -g) $HOME/.kube/config

mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

# Network!
wget https://docs.projectcalico.org/manifests/calico.yaml
# sed -i 's/192.168.0.0\/16/10.10.0.0\/16/g' calico.yaml
kubectl apply -f calico.yaml

kubectl get nodes
# Done installation!

# WEB UI
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml

# Create a user account
kubectl create serviceaccount dashboard-admin-sa
kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa

# Get secret from the account
kubectl get secrets
kubectl describe secret dashboard-admin-sa-token-d6ld4

# Start proxy
#kubectl proxy --address='0.0.0.0' --port=8080 --accept-hosts='.*' &
kubectl proxy &

# On local machine in a separate window:
ssh -L 8080:127.0.0.1:8001 -N -f -l kot@192.168.26.26
### http://192.168.26.26:8080/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

# Local URL to connect
# http://localhost:8080/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
kubectl get services -n kubernetes-dashboard

# Generate tocket to connect
sudo kubeadm token list

sudo kubeadm token create
openssl x509 -pubkey \
-in /etc/kubernetes/pki/ca.crt | openssl rsa \
-pubin -outform der 2>/dev/null | openssl dgst \
-sha256 -hex | sed 's/ˆ.* //'

# (stdin)= 9ebe115403f549f1b57e82c1a88b74bba741b4ad0f22f3159eef2f1f31b78833

#kubeadm join \
#--token et7o7r.xv8urw3e0shmp99b \
#centos8.local:6443 \
#--discovery-token-ca-cert-hash \
#sha256:9ebe115403f549f1b57e82c1a88b74bba741b4ad0f22f3159eef2f1f31b78833

# Post configuration

kubectl describe node | grep -i taint
# Remove restriction
kubectl taint nodes --all node-role.kubernetes.io/master-
kubectl describe node | grep -i taint

#
kubectl get pods --all-namespaces



############################### Deployment ###########################
kubectl create deployment nginx --image=nginx

# Save deoployment into file
kubectl get deployment nginx -o yaml > nginx.yaml

# Edit file
# into file
name: nginx
ports:                               # Add these8
- containerPort: 80                  # three
  protocol: TCP                      # lines

# Update deployment
kubectl replace -f nginx.yaml

# Get info about deployment
kubectl get deploy,pod
# Check null
kubectl get svc nginx

# Expose service and get again
kubectl expose deployment/nginx
kubectl get svc nginx

# get endpoint for the nginx
kubectl get ep nginx

# Get info about pod
kubectl describe pod nginx


kubectl scale deployment nginx --replicas=3
kubectl get deployment nginx

kubectl get ep nginx
# Finde where
kubectl describe pod nginx | grep Node

# Delete particular pod
kubectl delete pod nginx-7848d4b86f-g59hz

kubectl get po
# System recreate pod immediatly.

# Check container info
kubectl exec nginx-7848d4b86f-rcmbm -- printenv | grep KUBERNETES

# Delete service
kubectl delete svc nginx

# Create a new service with different type
kubectl expose deployment nginx --type=LoadBalancer

firewall-cmd --permanent --add-port=30933/tcp --zone=external
firewall-cmd --reload

# Remove 
kubectl delete deployments nginx
kubectl delete svc nginx
