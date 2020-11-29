# Maintenance


sudo grep data-dir /etc/kubernetes/manifests/etcd.yaml


# Login into etcd
#1. List all pods
kubectl get po --all-namespaces
#2. Enter into the pod
kubectl -n kube-system exec -it etcd-k8smaster.local -- sh

# Test environment
kubectl -n kube-system exec -it etcd-k8smaster.local -- sh \
    -c "ETCDCTL_API=3 \ #Version to use
    ETCDCTL_CACERT=/etc/kubernetes/pki/etcd/ca.crt \
    ETCDCTL_CERT=/etc/kubernetes/pki/etcd/server.crt \
    ETCDCTL_KEY=/etc/kubernetes/pki/etcd/server.key \
    etcdctl endpoint health"   #The command to test the endpoint

# Check how much DBs we have
kubectl -n kube-system exec -it etcd-k8smaster.local -- sh \
    -c "ETCDCTL_API=3 etcdctl \
    --cert=./peer.crt \
    --key=./peer.key \
    --cacert=./ca.crt \
    --endpoints=https://127.0.0.1:2379 member list"

# Check in table
kubectl -n kube-system exec -it etcd-k8smaster.local -- sh \
    -c "ETCDCTL_API=3 \
    ETCDCTL_CACERT=/etc/kubernetes/pki/etcd/ca.crt \
    ETCDCTL_CERT=/etc/kubernetes/pki/etcd/server.crt \
    ETCDCTL_KEY=/etc/kubernetes/pki/etcd/server.key  \
    etcdctl --endpoints=https://127.0.0.1:2379 \
    -w table endpoint status --cluster"  #<-- Note the addition of -w table

# Save snapshot
kubectl -n kube-system exec -it etcd-k8smaster.local -- sh \
    -c "ETCDCTL_API=3 \
    ETCDCTL_CACERT=/etc/kubernetes/pki/etcd/ca.crt \
    ETCDCTL_CERT=/etc/kubernetes/pki/etcd/server.crt \
    ETCDCTL_KEY=/etc/kubernetes/pki/etcd/server.key \
    etcdctl --endpoints=https://127.0.0.1:2379 \
    snapshot save /var/lib/etcd/snapshot.db"

# Chech that file is there
ls -l /var/lib/etcd/

# Simple Backup
mkdir $HOME/backup
cp /var/lib/etcd/snapshot.db $HOME/backup/snapshot.db-$(date +%m-%d-%y)
cp /root/kubeadm-config.yaml $HOME/backup/
cp -r /etc/kubernetes/pki/etcd $HOME/backup/


######################## Work with memory utilization ################################

# Create a deployment with stress testscub
kubectl create deployment hog --image vish/stress


kubectl get deployments
kubectl describe deployment hog
kubectl describe pod hog | grep Node

# Save config to modify in future
kubectl get deployment hog -o yaml > hog.yaml

# Change resourses block
'''
imagePullPolicy: Always3
name: hog4
resources:                   
  limits:                     
    memory:"4Gi"
  requests:
    memory:"2500Mi"
terminationMessagePath: /dev/termination-log
terminationMessagePolicy: File
'''
kubectl replace -f hog.yaml

kubectl get po
kubectl logs hog-5bf9d6f59-rrn84

kubectl scale deployment hog --replicas=3
