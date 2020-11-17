#!/usr/bin/python3
import subprocess
import time

proc = subprocess.Popen(['ls', '-l'])

time.sleep(10)

proc.communicate()
time.sleep(5)