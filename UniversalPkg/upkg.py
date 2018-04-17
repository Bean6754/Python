#!/usr/bin/python3

import argparse
import platform
import system

# Check root.
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nExiting.")

# dist = platform.dist() - Depreciated since Python 2.6.
dist = platform.linux_distribution()
# jar = platform.java_ver()
win = platform.win32_ver()
mac = 


if "mac" in mac:
  exit("This software only works with GNU/Linux.\nSorry.")
if "win" in win:
  exit("This software only works with GNU/Linux.\nSorry.")
# print(dist)

# Argparse.
parser = argparse.ArgumentParser()
parser.add_argument("-u", help="Update system.")
args = parser.parse_args()
if args.u:
    print("Updating system.")
    # If statements.
    if "arch" in dist:
      system(pacman -Syyu)
    if "centos" in dist:
      system(yum update -y)
    if "fedora" in dist:
      system(dnf update -y)
      system(yum update -y) # For compatibility reasons. :(
    if "debian" in dist:
      system(apt-get update)
      system(apt-get upgrade -y)
      system(apt-get dist-upgrade -y)
      system(apt-get full-upgrade -y)
    if "Ubuntu" in dist:
      system(apt-get update)
      system(apt-get upgrade -y)
      system(apt-get dist-upgrade -y)
      system(apt-get full-upgrade -y)
