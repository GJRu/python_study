#coding:utf-8
#函数
L = []
x = 1
while x <= 100:
    L.append(x * x)
    x = x + 1
print sum(L)
print abs(-7)
print int('123')
print str('999')
print cmp(3,4),cmp(3,3),cmp(4,3)

def cheng_sum(L):
    sum = 0
    for a in L:
        sum = sum + abs(a)
    return sum 
print cheng_sum([3.8, -5])
print cheng_sum([-7, 8])

import math
print math.sqrt(9)

def move(n, a, b, c):     #汉诺塔递归
    if n == 1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)
move(4, 'A', 'B', 'C')

def greet(x = None):        #默认参数
    if x == None:
        print 'Hello,world.'
    else:
        print 'Hello,xxx.'
greet()
greet('Bart')

def average(*args):
    sum = 0.0
    if len(args)==0:
        return sum
    else:
        for x in args:
            sum = sum + x
        return sum/len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)