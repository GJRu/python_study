class Person(object):
    count = 0
    __count = 0
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        Person.count = Person.count + 1
        Person.__count = Person.__count + 1
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score > 60 and self.__score < 70:
            return 'B'
        else:
            return 'C'
bob = Person('Bob', 95)
mary = Person('Mary', 67)
kim = Person('Kim', 30)
print bob.get_grade()
print mary.get_grade()
print kim.get_grade()
print Person.count
try:
    print Person.__count
except:
    print 'error'
print bob == mary
l1 = [bob, mary, kim]
l2 = sorted(l1, lambda x, y: cmp(x.name, y.name))
print l2[0].name, l2[1].name, l2[2].name 




class Person(object):
    def __init__(self, name, gender, birth, weight, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__weight = weight  
        for k, v in kw.iteritems():
            setattr(self, k, v)

mary = Person('mary', 'Male', '2005-1-1', 63, job = 'Student')
print mary.name
print mary.job
try:
    print mary.__weight
except:
    print 'error'



class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()



class Person(object): 
    __count = 0
    @classmethod
    def num(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1
print Person.num()
p1 = Person('Bob')
print Person.num()