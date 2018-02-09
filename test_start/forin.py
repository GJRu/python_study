#coding:utf-8   for in
L = range (1, 50)
for i in L:
    if i % 2 == 0:
        print i 

L = ['aaa', 'bbb', 'ccc', 'ddd']
for index, x in enumerate(L):
    print index+1, ': ', x      #zip  合并
for index, x in zip(range(1, len(L)+1),L):
    print index, ': ',x 

L = {'aaa': 11,'bbb': 22,'ccc': 33}
sum = 0.0
for s in L.itervalues():
    sum = sum + s
print sum / len(L)
print L.items()
for p, q in L.items():
    print p,': ',q

