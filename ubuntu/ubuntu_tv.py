#!/usr/bin/python3
""" This is a file for TV setup and configuration"""
import subprocess
import webbrowser

subprocess.Popen("lsb_release -a", shell=True)
# Colore codes
CGREEN = '\33[32m'
CEND = '\033[0m'

#Set packet lists
PACKAGES = """
net-tools wget git xclip
software-properties-common apt-transport-https
python3-pip
apt-transport-https ca-certificates curl gnupg-agent software-properties-common
chrome-gnome-shell
openjdk-8-jdk openjdk-8-jre
"""
for package in PACKAGES.split():
    print(package)

#Get updates first
p = subprocess.Popen("apt update", shell=True)
p.wait()

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

def extensions():
    """ Install extensions into the GNOME """
    #bing
    url = "https://extensions.gnome.org/extension/1262/bing-wallpaper-changer/"
    webbrowser.get('firefox').open_new_tab(url)

    url = "https://extensions.gnome.org/extension/750/openweather/"
    webbrowser.get('firefox').open_new_tab(url)

myinstall(PACKAGES)
