#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Code By n0rkeyys

import os
import sys
import time
from os import system as s
from datetime import datetime

now = datetime.now()
s("clear")

s("termux-setup-storage")
s("apt update -y && apt upgrade -y")
s("pkg update -y && pkg upgrade -y")

s("pkg install git -y")
s("pkg install vim -y")
s("pkg install wget -y")
s("pkg install nmap -y")
s("pkg install openssh -y")
s("pkg install openssl -y")

s("pkg install ruby -y")
s("pkg install curl -y")
s("pkg install perl -y")
s("pkg install nodejs -y")

s("pkg install python -y")
s("pkg install python2 -y")
s("pkg install python3 -y")

s("python3 -m pip install --upgrade pip")
s("pip3 install termcolor")
s("pip3 install colorama")
s("pkg install figlet")

s("cd")
s("bash build.sh")
s("cd /usr/etc")
shell = open("bash.bashrc","w")
shell.write("""
#!/bin/bash
clear
figlet n0rkeyys
PS1="root@localhost-:# "
cd
""")
shell.close()
s("rm -r /data/data/com.termux/files/usr/etc/bash.bashrc")
s("mv bash.bashrc //data/data/com.termux/files/usr/etc")
import colorama
from colorama import Fore,Back,Style
s("clear")
colorama.init()
print(Fore.GREEN)
s("figlet n0rkeyys")
k = "*" * 20
print("{0} Date {1} {2}\n".format(k,now,k))
time.sleep(3)
s("exit")
