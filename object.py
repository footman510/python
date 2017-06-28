#!/usr/bin/python
class person:
 def __init__(self,name):
  self.name=name
 def say(self):
  print 'my name is',self.name
p=person('Jack')
p.say()
