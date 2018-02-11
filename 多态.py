class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender 
    def whop(self):
        return 'person-----' + self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whop(self):
        return 'student-----' + self.name

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whop(self):
        return 'teacher-----' + self.name
class Book(object):
    def whop(self):
        return 'book-----'

per = Person('pname', 'pgender')
stu = Student('sname', 'sgender', 'sscoure')
tea = Teacher('tname', 'tgender', 'tcourse')
bok = Book()
def wp(ty):
    print ty.whop()
wp(per)
wp(stu)
wp(tea) 
wp(bok)


