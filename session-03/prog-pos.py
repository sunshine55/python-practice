#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser()

# LET'S ADD POSITIONAL ARGUMENTS
# add_argument
# - dest    the name which is used to access the argument
parser.add_argument("username")
parser.add_argument("timeout")

args = parser.parse_args()

username = args.username
print "Username: %s" % username