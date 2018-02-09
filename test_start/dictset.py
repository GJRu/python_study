#!/usr/bin/python   dict
#coding:utf-8
d = {
    'aaa': 30,
    'bbb': 50,
    'ccc': 80
}
print len(d)
print 'aaa', d['aaa']
print d.get('bbb')
print d.get('ddd')

d['ddd'] = 90
print d

for key in d :
    print key + ':', d[key]

s = set (['aaa','bbb','ccc','ccc'])  #无序  set
print s
print 'aaa' in s

score = set ([111, 222, 333, 'aaa'])
sx = 000
if sx in score: 
    print 'ok'
else :
    print 'no' 

for sh in score :
    print sh

#g = ['111', 'bbb', 'eee']
for some in score :
    if some in s :
        s.remove(some)
    else:
        s.add(some)
print s 