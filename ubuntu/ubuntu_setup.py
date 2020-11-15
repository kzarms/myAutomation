#!/usr/bin/python3
""" This is main module dockstring"""
import subprocess
import webbrowser

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

def ssh_keys(my_mail):
    """ Default packages installation function """
    #
    if not my_mail:
        my_mail = input('Enter your email:')
    cmd = 'ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -C "' + my_mail + '" -q -N ""'
    my_p6 = subprocess.Popen(cmd, shell=True)
    my_p6.wait()
    print(CGREEN + "4k keys generated successfully" + CEND)

myinstall(PACKAGES)
VScode()
#MSTeams()
extensions()
#my_docker()
