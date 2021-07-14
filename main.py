import os
import random
from time import sleep
import urllib.request
import urllib.parse
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
def internet():
    try:
        urllib.request.urlopen('https://www.google.com')
    except Exception:
        print("You are not connected To Internet!!!")
        print("\tPlease Connect To Internet To Continue...\n")
        input('Exiting....\n Press Enter To Continue....')
        exit()
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
vio = '\033[1;35m'
non = '\033[1;0m'
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def lgo():

    colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']
    W = '\033[0m'

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def logo():
        clr()
        sleep(1)
        lg = """\033[1;34m
              .888888888.               888                         
              0000    0000              000                              
              888      888              888
              888           R8888888R   888                            
              000           R8888888R   000                               
              888     000               888          88  
              0000   0000               0000        000                    
              "000000000"               88888888888888     
       \033[1;0m"""
        print(lg)
        sleep(1)

    def banner():
        clr()
        logo = """" 
              .888888888.               888                         
              0000    0000              000                              
              888      888              888
              888           R8888888R   888                            
              000           R8888888R   000                               
              888     000               888          88  
              0000   0000               0000        000                    
              "000000000"               88888888888888     

          \033[1;34m        Developed By :\033[1;34m Al Jabir   """
        print(random.choice(colors) + logo + W)
        print("\n")

    logo()
    banner()
    print(red + "\n::::::::::::::::::::::::::::::::::::::::::")
def pas():
    z = 0
    while z!= 1:
        a = input("Username: ")
        b = input("Password: ")
        if a == "hello" and b == "12" :
            print("Password matched!")
            clr()
            break
        else:
            print("Password not matched!")
            clr()

            continue
lgo()
pas()
lgo()
print(green + "\n\t\tChecking for update.....")
sleep(1)
def up():
    a = requests.get('https://pastebin.com/raw/H9vBwhBb').text
    if a == "Update":
        lgo()
        print("\n\n\t\tC-L is bing  updated.....")
        sleep(1)
        os.system('cd $HOME')
        os.system('rm -rf C-L_updater')
        os.system('git clone https://github.com/Cyber-log/C-L_updater')
        sleep(0.7)
        os.system('cd $HOME && cd C-L_updater')
    else:
        lgo()
        print(red + "\n::::::::::::::::::::::::::::::::::::::::::")
        print(green + "\n\t\tC-L is updated.")
        sleep(2)
        clr()
up()
def banner():
    colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']
    W = '\033[0m'

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    clr()
    logo = """" 
  .888888888.               888                         
  0000    0000              000                              
  888      888              888
  888           R8888888R   888                            
  000           R8888888R   000                               
  888     000               888          88  
  0000   0000               0000        000                    
  "000000000"               88888888888888     

      \033[1;34m        Developed By :\033[1;34m Al Jabir   """
    print(random.choice(colors) + logo + W)
    print("\n")
def rn():
    e = ""
    banner()
    print(red + e)
    print(vio + "\n\n\n==>Select a option from below")
    print(yellow + "\n\n1. BD Sms Bomber"
                   "\n2. E-mail Bomber")
    ch = str(input(blue + "[^} Enter a option: "+red))
    if ch == '1':
        os.system('python smsbomb.py')
    elif ch == '2':
        os.system('python emailbomber.py')
    elif ch == '3':
        print(blue + "\t\t\t\t\tCyber Log"
                     "\t\t\tFacebook  Profile: https://m.facebook.com/al.jabir.543"
                     "\t\t\tFacebook Page    : https://m.facebook.com/Cyber-Log-105754961789563/"
                     "\t\t\tFacebook Group   : https://facebook.com/groups/850478649236281/"
                     "\t\t\tGithub           : https://github.com/Cyber-log")

    else:
        e = (red + "You entered a wrong option")

