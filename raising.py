#!/usr/bin/python
class shortinputexception(Exception):
 def __init__(self,length,atleast):
  Exception.__init__(self)
  self.length=length
  self.atleast=atleast
try:
 s=raw_input('enter something:')
 if len(s)<5:
  raise shortinputexception(len(s),5)
except EOFError:
 print '\nwhy did you do an EOF on me?'
except shortinputexception:
 print 'error! the length of input is atleast 5.'
else:
 print 'done.'


