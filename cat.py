#!/usr/bin/python
import sys
def readfile(fname):
 f=file(fname)
 while True:
  line=f.readline()
  if len(line)==0:
   break
  print line,
 f.close()
if len(sys.argv)<2:
 print 'no action specified'
 sys.exit()
if sys.argv[1].startswith('--'):
 option=sys.argv[1][2:]
 if option=='version':
  print 'Version 1'
 elif option=='introduce':
  print 'Display your txt.'
 elif option=='help':
  print '''
--version :Prints the version.
--help    :Display this help.'''
  sys.exit()
 else:
  print 'unknown option'
else:
 for fname in sys.argv[1:]:
  readfile(fname)
