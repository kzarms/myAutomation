#!/usr/bin/bash
# chmod +x k8s_install.sh
# sudo ./k8s_install.sh

echo "Simple installating K8S on the node."
# Run on Centos8
dnf update
dnf upgrade

# Add Static names for DNS
echo "192.168.0.254 centos8.local" | tee -a /etc/hosts
echo "192.168.0.21 node1.local" | tee -a /etc/hosts
echo "192.168.0.22 node2.local" | tee -a /etc/hosts

# Disable SElinux and swap file
setenforce 0

sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
# reboot

# Firewall Setup
firewall-cmd --permanent --add-port=6443/tcp
firewall-cmd --permanent --add-port=8001/tcp
firewall-cmd --permanent --add-port=8080/tcp
firewall-cmd --permanent --add-port=2379-2380/tcp
firewall-cmd --permanent --add-port=10250/tcp
firewall-cmd --permanent --add-port=10251/tcp
firewall-cmd --permanent --add-port=10252/tcp
firewall-cmd --permanent --add-port=10255/tcp
firewall-cmd --reload
# disable swap
swapoff -a

# Remove 
dnf remove podman buildah -y

# Add docker repo
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo

# Install docker
dnf install docker-ce -y

# Check
docker --version

# Start service
systemctl enable docker
systemctl start docker

systemctl status docker

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

cat <<EOF > kubeadm-config.yaml
apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
# kubernetesVersion: 1.18.1                   #<-- Use the word stable for newest version
controlPlaneEndpoint: "centos8.local:6443"  #<-- Use the node alias not the IP
networking:
    podSubnet: 10.10.0.0/16                 #<-- Match the IP range from the Calico config file
EOF

# Init the claster
kubeadm init --config=kubeadm-config.yaml --upload-certs | tee kubeadm-init.out # Save output for future review

# Network!
wget https://docs.projectcalico.org/manifests/calico.yaml
kubectl apply -f calico.yaml

kubectl get nodes
# Done installation!

# WEB UI
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml

# Create a user account
kubectl create serviceaccount dashboard-admin-sa
kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa

kubectl get secrets
kubectl describe secret dashboard-admin-sa-token-d6ld4

# Start proxy
#kubectl proxy --address='0.0.0.0' --port=8080 --accept-hosts='.*' &
kubectl proxy

ssh -L 8080:127.0.0.1:8001 -N -f -l kot 192.168.26.26


http://192.168.26.26:8080/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

http://localhost:8080/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
kubectl get services -n kubernetes-dashboard


# Start
#systemctl enable kubelet
#systemctl start kubelet

# init
#swapoff -a
#kubeadm init


kubeadm join 192.168.0.254:6443 --token u4taeh.8bzkaq72okfwqpnc --discovery-token-ca-cert-hash sha256:7c75287b770adbf46cc9980d704338254b98c0568127719e54c5326c16e59072
kubectl proxy --address='0.0.0.0' --port=8080


# Install web board
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml

kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa




You can now join any number of the control-plane node running the following command on each as root:

  kubeadm join centos8.local:6443 --token 93jtl2.c1ntx3ekmfk9qyox \
    --discovery-token-ca-cert-hash sha256:fda96dc41017d3ee5b4a0d2c1cce9de07b2774a6e0604929481f41b51cd8083b \
    --control-plane --certificate-key 55f1904c4d06c5e53a28ede6420441448b85fa549d899da554aad903044cb1a5

Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use
"kubeadm init phase upload-certs --upload-certs" to reload certs afterward.

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join centos8.local:6443 --token 93jtl2.c1ntx3ekmfk9qyox \
    --discovery-token-ca-cert-hash sha256:fda96dc41017d3ee5b4a0d2c1cce9de07b2774a6e0604929481f41b51cd8083b
