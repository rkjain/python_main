#!/usr/bin/env python


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name', help='prints your name')
parser.add_argument('--version','-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

print args.name
