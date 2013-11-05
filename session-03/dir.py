#!/usr/bin/python

from sys import argv

print argv

if '-h' in argv or '--help' in argv:
    print 'HELP is not ready'

elif len(argv)==3:
    path = argv[1]
    if argv[1]=='-o':
        show_dotted = True
    else:
        show_dotted = False
    import os
    print 'List directory content (without dotted files)'
    for item in os.listdir(path):
		print item
    
elif len(argv)==2:
    path = argv[1]
    show_dotted = False
    
    import glob
    
    print 'List directory content (dotted files included)'
    for item in glob.glob(path):
		print item