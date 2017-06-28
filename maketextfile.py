#!/usr/bin/python
import os
ls=os.linesep
while True:
 fname=raw_input('input a filename:\n')
 if os.path.exists(fname):
  print "error: '%s' already exists!" %fname
 else: 
  break
all=[]
print "\nenter each line:(end with '#')\n"
while True:
 entry=raw_input('>')
 if entry=='#':
  break
 else:
  all.append(entry)
f=open(fname,'w')
f.writelines(['%s%s' % (x,ls) for x in all])
f.close()
print 'Done'
