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
ping node1.local -c1
ping www.google.com -c1
# disable swap
swapoff -a
# cat /etc/fstab
sed -i 's/\/dev\/mapper\/cl-swap/\#\/dev\/mapper\/cl-swap/g' /etc/fstab
# Disable local firewall
systemctl stop firewalld
systemctl disable firewalld
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

kubeadm join k8smaster.local:6443 --token jp4z7c.b2ebxh4wshy6t6nx --discovery-token-ca-cert-hash sha256:407a16a80e06e1fc95aee2505d59a92bb1ff6a76dab23580272787f7d13fb904 --control-plane --certificate-key aa0eae7ea0ac6fa6b78904f6c8862c0ae04f964a52614c420264950ad4da294b