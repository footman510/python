#!/usr/bin/python
while True:
 s=raw_input('enter a string:')
 if s=='quit':
  break
 if len(s)<3:
  continue
 print'the length of the string is',len(s)
print 'done'
