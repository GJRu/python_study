#coding:utf-8
def log(cal):
    def fnew(x):
        print 'call' + cal.__name__ + '()'
        return cal(x)
    return fnew
@log      #只含有一个参数的返回函数
def calcul(num):
    return reduce(lambda x,y: x * y, range(1, num+1))
print calcul(5)


import time
def performance(fac):
    def fnew(*args, **kw):  #确保任意参数个数
        start = time.time()
        fac(*args, **kw)
        end = time.time()
        print 'call ' + fac.__name__ + '()..in ' + str(end - start)
        return fac(*args, **kw)
    return fnew
@performance
def factorial(num):
    return reduce(lambda x,y: x*y, range(1, num+1))
print factorial(10)


import time
import functools
def performance(unit):
    def newfac(fac):
        @functools.wraps(fac)
        def war(*args, **kw):
            start = time.time()
            print start
            fac(*args, **kw)
            end = time.time()
            print end
            if unit == 'ms':
                ti = (end - start)* 1000 
            else:
                ti = end - start
            print 'call!!! ' + fac.__name__ + '() in ' + str(ti)
            return fac(*args, **kw)
        return war
    return newfac
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
print factorial.__name__


import functools           #偏函数
strfiro = functools.partial(sorted, cmp = lambda x, y:(cmp(x.upper(), y.upper())))
print strfiro(['Gaa', 'bbb', 'Acc'])