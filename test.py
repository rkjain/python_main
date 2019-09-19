#!/usr/bin/env python3

import subprocess
import sys
import shlex


def command_chainer(*args):
	for command in args:
		commander(command)


def commander(cmd):
    x = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True)
    if x.stdout:
        print("Output: ")
        print(x.stdout)
    if x.stderr:
        print("Error Message: ")
        print(x.stderr)
        sys.exit(1)

command_chainer('ls -ltr', 
    'df -H ./',
	'ping -c 4 www.google.com',
	'whoami',
	'hostname')

