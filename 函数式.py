#coding:utf-8
import math
a = abs
print abs(-5)

def calcu(x, y, funct):    #函数通过变量传给另一个函数
    return funct(x) + funct(y)
print calcu(6, -9, abs)
print calcu(25, 9, math.sqrt)

def strfirup(L):
    return L[0].upper() + L[1:].lower()
print map(strfirup, ['aaa', 'bbb','ccc']) #map()内置高阶函数一个

def prod(x, y):
    return x * y 
print reduce(prod, [1, 3, 4, 5],2)  #reduce()内置高阶函数两个参数

def sqrodd(x):
    return math.sqrt(x) % 2 == 0
print filter(sqrodd, range(1, 101)) #fliter()筛选出符合条件返回true,false

print filter(lambda x: math.sqrt(x) % 5 == 0,range(1,101))
#lambda 匿名函数 不用单写函数 直接创建函数对象

def cmpnum(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0
print sorted([4, 2, 6, 1, 5], cmpnum)  #sorted()函数用于排序

def caldefer(L):
    def cade():  #延迟计算
        def fe(x, y):
            return x * y 
        return reduce(fe, L)  #list各元素计算
    return cade
fe = caldefer([1, 2, 3, 1])
print fe()

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(),f2(),f3()   #变量i的值已经变成了3

def count():
    fs = []
    for i in range(1, 4):
        j = i
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))  #避免循环变量i的值的影响
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()