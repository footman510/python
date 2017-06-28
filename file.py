#!/usr/bin/python
filename=raw_input('Enter file name:')
f=file(filename,'r')
for e in f:
  print e,
f.close()
