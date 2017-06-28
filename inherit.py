#!/usr/bin/python
class schoolmember:
 '''Represents any school member.'''
 def __init__(self,name,age):
  self.name=name
  self.age=age
  print 'Initialized schoolmember:%s' % self.name
 def tell(self):
  '''Tell my details.'''
  print 'name:%s age:%s'%(self.name,self.age),
class teacher(schoolmember):
 '''Represents a teacher.'''
 def __init__(self,name,age,salary):
  schoolmember.__init__(self,name,age)
  self.salary=salary
  print 'Initialized teacher:%s' % self.name
 def tell(self):
  '''Tell my details.'''
  schoolmember.tell(self)
  print 'salary:%s' % self.salary
class student(schoolmember):
 '''Represents a student.'''
 def __init__(self,name,age,marks):
  schoolmember.__init__(self,name,age)
  self.marks=marks
  print 'Initialized student:%s' % self.name
 def tell(self):
  '''Tell my details.'''
  schoolmember.tell(self)
  print 'marks:%s' % self.marks
sm=schoolmember('abc','40')
sm.tell()
s=student('ab','18','80')
s.tell()
t=teacher('cc','35','4000')
t.tell()
