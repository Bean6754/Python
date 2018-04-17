#!/usr/bin/python3

import argparse     # Needed for program earguments.
import os           # Needed for check EUID (root or not).
import time         # This is required to include time module.

# Check root.
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nExiting.")

ticks = time.time()
if ticks < 1523975512:
  exit("Please set your system's date and time.\n")
