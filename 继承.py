class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender 

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

s1 = Student('smary', 'F', 80)
t1 = Teacher('tbob', 'm', 'english')
print s1.score
print t1.course

print isinstance(s1, object)
print isinstance(s1, Person)
print isinstance(s1, Student)
print isinstance(s1, Teacher)