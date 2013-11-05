#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser()

# LET'S ADD POSITIONAL ARGUMENTS
# add_argument
# - dest    the name which is used to access the argument
parser.add_argument('-x','--exec',dest='script',required=True,help="Execute the script file")
parser.add_argument('-u','--username',dest='username',help="Login as username")
parser.add_argument('-t','--type',type=int,choices=[1,2,3],dest='type',help="Access type")
parser.add_argument('-r','--recursive',
        action="store_true",dest='recursive',default=False,
        help="Recursive option")


args = parser.parse_args()

username = args.username
print "Username: %s" % username

if args.recursive:
    print 'RECURSIVE is dangerous...'