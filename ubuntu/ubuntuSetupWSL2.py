import subprocess
#import webbrowser

subprocess.Popen("lsb_release -a", shell=True)

#Set packet lists
#General packages
packages = "net-tools wget git xclip sshpass"
#Add pip3 install
packages += " " + "python3-pip"
#Add docker dependencies
#packages += " " + "apt-transport-https ca-certificates curl gnupg-agent software-properties-common"

for item in packages.split():
  print(item)

#Get updates first
p = subprocess.Popen("apt update", shell=True)
p.wait()

def myinstall(packages):
  CGREEN  = '\33[32m'
  CEND = '\033[0m'

  print(CGREEN + "[+] Installation of the ubuntu packages is starting:" + CEND)
  #Loop for all packages in the list
  for item in packages.split():
    command = "apt install " + str(item) + " -y"
    p = subprocess.Popen(command, shell=True)
    p.wait()
    print(CGREEN + f"\t[+] Package [{item}] Installed" + CEND)

  print(CGREEN + "[+] Installation of the ubuntu packages has been completed" + CEND)

#def extensions():
  #bing
#  url = "https://extensions.gnome.org/extension/1262/bing-wallpaper-changer/"
#  webbrowser.get('firefox').open_new_tab(url)

# url = "https://extensions.gnome.org/extension/750/openweather/"
# webbrowser.get('firefox').open_new_tab(url)

def VScode():
  CGREEN  = '\33[32m'
  CEND = '\033[0m'

  p = subprocess.Popen("wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add -", shell=True)
  p.wait()
  print(CGREEN + "Key has been added" + CEND)

  p = subprocess.Popen('add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"', shell=True)
  p.wait()
  print(CGREEN + "MS repository has been added"+  CEND)

  p = subprocess.Popen("apt update", shell=True)
  p.wait()
  p = subprocess.Popen("apt install code", shell=True)
  p.wait()
  print(CGREEN + "VSCode installed successfully" + CEND)

def MSTeams():
  CGREEN  = '\33[32m'
  CEND = '\033[0m'
  teams = "msteams.deb"

  command = 'wget -O ' + teams + ' "https://go.microsoft.com/fwlink/p/?linkid=2112886&clcid=0x409&culture=en-us&country=us"'
  p = subprocess.Popen(command, shell=True)
  p.wait()
  print(CGREEN + "MS Teams has been downloaded" + CEND)

  p = subprocess.Popen(("apt install ./" + teams), shell=True)
  p.wait()
  #Clean files
  subprocess.Popen(("rm " + teams), shell=True)
  print(CGREEN + "MS Teams installed successfully" + CEND)

def Docker():
  CGREEN  = '\33[32m'
  CEND = '\033[0m'
  #   https://docs.docker.com/engine/install/ubuntu/
  #Add key
  p = subprocess.Popen("wget -q https://download.docker.com/linux/ubuntu/gpg -O- | apt-key add -", shell=True)
  p.wait()
  print(CGREEN + "Docker key has been added" + CEND)
  #Add repo
  command = 'add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"'
  #command = 'add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"'
  p = subprocess.Popen(command, shell=True)
  p.wait()
  print(CGREEN + "Docker repository has been added" + CEND)
  #Install docker
  p = subprocess.Popen("apt update", shell=True)
  p.wait()
  p = subprocess.Popen("apt install docker-ce docker-ce-cli containerd.io -y", shell=True)
  p.wait()
  print(CGREEN + "Docker has been installed" + CEND)

  #Add user to the group
  p = subprocess.Popen("usermod -aG docker $USER", shell=True)
  p.wait()
  #Download docker-compose
  # sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  # sudo chmod +x /usr/local/bin/docker-compose
  #p = subprocess.Popen("wget -q https://download.docker.com/linux/ubuntu/gpg -O- | apt-key add -", shell=True)
  #p.wait()
  #print(CGREEN + "Docker key has been added" + CEND)

def Jenkins():
  CGREEN  = '\33[32m'
  CEND = '\033[0m'
  #   https://www.jenkins.io/doc/book/installing/#linux
  #Add key
  p = subprocess.Popen("wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | apt-key add -", shell=True)
  p.wait()
  print(CGREEN + "Jenkins key has been added" + CEND)
  #Add repo
  command = 'add-apt-repository "deb https://pkg.jenkins.io/debian binary/"'
  p = subprocess.Popen(command, shell=True)
  p.wait()
  print(CGREEN + "Jenkins repository has been added" + CEND)
  #Install docker
  p = subprocess.Popen("apt update", shell=True)
  p.wait()
  p = subprocess.Popen("apt install jenkins -y", shell=True)
  p.wait()
  print(CGREEN + "Jenkins has been installed" + CEND)

  #Add user to the group
  p = subprocess.Popen("usermod -aG docker $USER", shell=True)
  p.wait()

def sshKeys(myMail):
  CGREEN  = '\33[32m'
  CEND = '\033[0m'

  if not myMail:
    myMail = input('Enter your email:')
  cmd = 'ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -C "' + myMail + '" -q -N ""'
  p = subprocess.Popen(cmd, shell=True)
  p.wait()
  print(CGREEN + "4k keys generated successfully" + CEND)

myinstall(packages)
#VScode()
#MSTeams()
#extensions()
#Docker()
#Jenkins()