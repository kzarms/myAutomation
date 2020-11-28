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
# setenforce 0

# sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
# reboot

# Firewall Setup
firewall-cmd --permanent --add-port=6443/tcp
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
# kubeadm init --config=kubeadm-config.yaml --upload-certs | tee kubeadm-init.out # Save output for future review
kubeadm init --control-plane-endpoint 'centos8.local' --pod-network-cidr '10.10.0.0/16' --service-cidr '10.20.0.0/16' --upload-certs | tee kubeadm-init.out
# Exit form sudo mode
exit

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

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


# Start
#systemctl enable kubelet
#systemctl start kubelet

# init
#swapoff -a
#kubeadm init

