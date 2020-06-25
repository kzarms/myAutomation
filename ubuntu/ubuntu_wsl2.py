""" This is a file for wsl2 setup and configuration"""

import subprocess
#import webbrowser

subprocess.Popen("lsb_release -a", shell=True)

#Set packet lists
#General packages
PACKAGES = "net-tools wget git xclip sshpass"
#Add pip3 install
PACKAGES += " " + "python3-pip"
#Add docker dependencies
#packages += " " + "apt-transport-https ca-certificates curl gnupg-agent software-properties-common"
#Add ansible dependencies
#
# Nothing
CGREEN = '\33[32m'
CEND = '\033[0m'

for package in PACKAGES.split():
    print(package)

#Get updates first
my_p = subprocess.Popen("apt update", shell=True)
my_p.wait()

def myinstall(packages):
    """ Package installation fucntion """
    print(CGREEN + "[+] Installation of the ubuntu packages is starting:" + CEND)
    #Loop for all packages in the list
    for item in packages.split():
        command = "apt install " + str(item) + " -y"
        intp = subprocess.Popen(command, shell=True)
        intp.wait()
        print(CGREEN + f"\t[+] Package [{item}] Installed" + CEND)

    print(CGREEN + "[+] Installation of the ubuntu packages has been completed" + CEND)

myinstall(PACKAGES)
