import subprocess
import webbrowser


subprocess.Popen("lsb_release -a", shell=True)
#Set packet lists
packages = """
net-tools wget git xclip
software-properties-common apt-transport-https
python3-pip
chrome-gnome-shell
"""
for item in packages.split():
  print(item)

#Get updates first
p = subprocess.Popen("apt update", shell=True)
p.wait()

def myinstall(packages):
  CGREEN  = '\33[32m'
  CEND = '\033[0m'

  apt = "apt "
  ins = "install "
  #packages = "net-tools"
  print(CGREEN + "[+] Installation of the ubuntu packages is starting:" + CEND)
  #color.print_green("[+] Installation of the ubuntu packages is starting:")
  for item in packages.split():
    command = str(apt) + str(ins) + str(item) + " -y"
    #process = subprocess.run(command)
    p = subprocess.Popen(command, shell=True)
    p.wait()
    print(CGREEN + "\t[+] Package [{}] Installed".format(str(item)) + CEND)

def extensions():
  #bing
  url = "https://extensions.gnome.org/extension/1262/bing-wallpaper-changer/"
  webbrowser.get('firefox').open_new_tab(url)

  url = "https://extensions.gnome.org/extension/750/openweather/"
  webbrowser.get('firefox').open_new_tab(url)

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