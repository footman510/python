#!/usr/bin/python
class person:
 '''Represents a person'''
 popu=0
 def __init__(self,name):
  '''Initializes the person\'s data.'''
  self.name=name
  print 'Initializeing %s' % self.name
  person.popu+=1
 def __del__(self):
  '''I am dying.'''
  print '%s say goodbye' % self.name
  person.popu-=1
  if person.popu==0:
   print 'I am the last one.'
  else:
   print 'Threre are still %d people left.' % person.popu
 def say(self):
  '''Greeting by the person.
  
  Really, that\'s all it does.'''
  print 'my name is %s.' % self.name
 def howmany(self):
  '''Prints the current population.'''
  if person.popu==1:
   print 'I am the only person here.'
  else:
   print 'We have %d persons here.' % person.popu
Jack=person('Jack')
Jack.say()
Jack.howmany()

liyang=person('liyang')
liyang.say()
liyang.howmany()

Jack.say()
Jack.howmany()

del Jack
del liyang

