class A(object):
    pass
class B(A):
    pass


class a(object):
    pass
class b(a):
    def dxie(self):
        return 'bbbbbb'

class bB(b, B):
    pass

bb = bB()
print bb.dxie()

class X(object):
    def __init__(self):
        print 'x'

class Y(object):
    def __init__(self):
        print 'y'

class Z(X, Y):
    def __init__(self):
        X.__init__(self)
        Y.__init__(self)
        print 'z'

z = Z()

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

stu = Student('sname', 'sgender', 'sscoure')
print type(stu)
print type(123)
#print dir(stu)
#print dir(123)

print filter(lambda x: x[0] != '_', dir(stu))
print getattr(stu, 'name')
setattr(stu, 'gender', 'ff')
print stu.gender