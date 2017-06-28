#!/usr/bin/python
list=['math','english','chinese']
yuan=('math','english','chinese')
dict={       'a':'about',
             'b':'bad',
             'c':'close',
             'd':'disc'
}
print list[0]
for a in list[0:-1]:
 print a
newlist=list[0:3]
newlist.append('science')
newlist.sort()
print newlist
print yuan
print len(newlist)
print dict['a']
del dict['a']
print dict
for first,word in dict.items():
 print 'first is %c,word is %s\n'% (first,word)
