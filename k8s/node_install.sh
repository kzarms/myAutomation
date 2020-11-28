#!/usr/bin/bash
# chmod +x node_install.sh
# sudo ./node_install.sh

echo "Simple installating a node."
# Run on Centos8
dnf update
dnf upgrade

# Add Static names for DNS
echo "192.168.0.254 k8smaster.local" | tee -a /etc/hosts
echo "192.168.0.21 node1.local" | tee -a /etc/hosts
echo "192.168.0.22 node2.local" | tee -a /etc/hosts
ping k8smaster.local -c4
# disable swap
swapoff -a
cat /etc/fstab
sed -i 's/\/dev\/mapper\/cl-swap/\#\/dev\/mapper\/cl-swap/g' /etc/fstab
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

# Configure node
kubeadm join \
--token et7o7r.xv8urw3e0shmp99b \
centos8.local:6443 \
--discovery-token-ca-cert-hash \
sha256:9ebe115403f549f1b57e82c1a88b74bba741b4ad0f22f3159eef2f1f31b78833
