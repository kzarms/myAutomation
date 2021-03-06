#!/usr/bin/python3
""" This is main module dockstring"""
import subprocess
import webbrowser
import os

subprocess.Popen("lsb_release -a", shell=True)
#Set packet lists
CGREEN = '\33[32m'
CEND = '\033[0m'
PACKAGES = """
net-tools wget git xclip
software-properties-common apt-transport-https
python3-pip
apt-transport-https ca-certificates curl gnupg-agent software-properties-common
chrome-gnome-shell
"""
for item in PACKAGES.split():
    print(item)

#Get updates first
my_p0 = subprocess.Popen("apt update", shell=True)
my_p0.wait()

def myinstall(packages):
    """ Default packages installation function """
    apt = "apt "
    ins = "install "
    #packages = "net-tools"
    print(CGREEN + "[+] Installation of the ubuntu packages is starting:" + CEND)
    #color.print_green("[+] Installation of the ubuntu packages is starting:")
    for item2 in packages.split():
        command = str(apt) + str(ins) + str(item2) + " -y"
        #process = subprocess.run(command)
        my_p1 = subprocess.Popen(command, shell=True)
        my_p1.wait()
        print(CGREEN + "\t[+] Package [{}] Installed".format(str(item2)) + CEND)

def extensions():
    """ This is my doc scring """
    #bing
    url = "https://extensions.gnome.org/extension/1262/bing-wallpaper-changer/"
    webbrowser.get('firefox').open_new_tab(url)
    #
    url = "https://extensions.gnome.org/extension/750/openweather/"
    webbrowser.get('firefox').open_new_tab(url)

def VScode():
    """ Default packages installation function """
    my_p2 = subprocess.Popen( \
        "wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add -", \
        shell=True)

    my_p2.wait()
    print(CGREEN + "Key has been added" + CEND)

    my_p2 = subprocess.Popen( \
        'add-apt-repository "deb [arch=amd64] ' \
        + 'https://packages.microsoft.com/repos/vscode stable main"', \
        shell=True)

    my_p2.wait()
    print(CGREEN + "MS repository has been added"+  CEND)

    my_p2 = subprocess.Popen("apt update", shell=True)
    my_p2.wait()
    my_p2 = subprocess.Popen("apt install code", shell=True)
    my_p2.wait()
    print(CGREEN + "VSCode installed successfully" + CEND)

def ms_teams():
    """ Default packages installation function """
    teams = "msteams.deb"

    command = 'wget -O ' + teams + \
        ' "https://go.microsoft.com/fwlink/p/?linkid=2112886&clcid=0x409&culture=en-us&country=us"'
    my_p3 = subprocess.Popen(command, shell=True)
    my_p3.wait()
    print(CGREEN + "MS Teams has been downloaded" + CEND)

    my_p3 = subprocess.Popen(("apt install ./" + teams), shell=True)
    my_p3.wait()
    #Clean files
    subprocess.Popen(("rm " + teams), shell=True)
    print(CGREEN + "MS Teams installed successfully" + CEND)

def my_docker():
    """ Default packages installation function """
    #   https://docs.docker.com/engine/install/ubuntu/
    #Add key
    my_p4 = subprocess.Popen( \
        "wget -q https://download.docker.com/linux/ubuntu/gpg -O- | apt-key add -", \
        shell=True)
    my_p4.wait()
    print(CGREEN + "Docker key has been added" + CEND)
    #Add repo
    command = 'add-apt-repository "deb [arch=amd64] ' \
      + 'https://download.docker.com/linux/ubuntu bionic stable"'
    my_p4 = subprocess.Popen(command, shell=True)
    my_p4.wait()
    print(CGREEN + "Docker repository has been added" + CEND)
    #Install docker
    my_p4 = subprocess.Popen("apt update", shell=True)
    my_p4.wait()
    my_p4 = subprocess.Popen("apt install docker-ce docker-ce-cli containerd.io -y", shell=True)
    my_p4.wait()
    print(CGREEN + "Docker has been installed" + CEND)

    #Add user to the group
    my_p4 = subprocess.Popen("usermod -aG docker $USER", shell=True)
    my_p4.wait()

def ssh_keys(my_mail=""):
    """ Default packages installation function """
    #
    keyFile = "/.ssh/id_rsa"
    if os.path.exists(os.path.expanduser("~")+keyFile):
        # key file exists
        print(CGREEN + "4k keys are existing. Exit." + CEND)
        return
    if not my_mail:
        my_mail = input('Enter your email:')
    cmd = 'ssh-keygen -t rsa -b 4096 -f ~' + keyFile + ' -C "' + my_mail + '" -q -N ""'
    subP = subprocess.Popen(cmd, shell=True)
    subP.wait()
    print(CGREEN + "4k keys generated successfully" + CEND)

def ansible():
    """ Prepare for ansible installation """
    # https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu
    print(CGREEN + "Installing Ansible package" + CEND)
    subP = subprocess.Popen('apt install software-properties-common', shell=True)
    subP.wait()
    subP = subprocess.Popen('apt-add-repository --yes --update ppa:ansible/ansible', shell=True)
    subP.wait()
    subP = subprocess.Popen('apt install ansible -y', shell=True)
    subP.wait()
    print(CGREEN + "Ansible has been installed successfully" + CEND)

def salt(slave=1):
    """ Prepare for salt-stack installation """
    # https://repo.saltstack.com/#ubuntu
    print(CGREEN + "Installing Ansible package" + CEND)
    subP = subprocess.Popen( \
        "wget -O - https://repo.saltstack.com/py3/ubuntu/20.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -", \
        shell=True)
    subP.wait()
    subP = subprocess.Popen( \
        'add-apt-repository "deb [arch=amd64] ' \
        + 'http://repo.saltstack.com/py3/ubuntu/20.04/amd64/latest focal main"', \
        shell=True)
    subP = subprocess.Popen('apt-get update', shell=True)
    subP.wait()
    if slave:
        subP = subprocess.Popen('apt-get install salt-minion -y', shell=True)
    else:
        subP = subprocess.Popen('apt-get install salt-master salt-minion salt-ssh salt-syndic salt-cloud salt-api -y', shell=True)
    subP.wait()
    print(CGREEN + "SaltStack has been installed successfully" + CEND)

#myinstall(PACKAGES)
#VScode()
#MSTeams()
#extensions()
#my_docker()
ssh_keys()
ansible()
# salt()
