#coding:utf-8
        
class Student(object):
    
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score
    
    def __cmp__(self, l):
        if self.score > l.score:
            return -1
        elif self.score < l.score:
            return 1
        else :
            if self.name > l.name:
                return 1
            elif self.name < l.name:
                return -1
            else:
                return 0

    def __len__():
        return 
    
    def __str__(self):
        return '<Student: %s, %s, %s>' %(self.name, self.gender, self.score)
    __repr__ = __str__   #显示给开发人员    显示给用户

s1 = Student('Bob', 'm', 88)
print s1
l1 = [Student('kim', 'm', 99), Student('bob', 'f', 88), Student('alic','m', 99), Student('mary', 'f', 60)]
print (l1)
print len(l1)
