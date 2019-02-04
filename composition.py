class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_details(self):
        return "%s's age is %s" % (self.name, self.age)

class Standard:
    def __init__(self, name, age, standard):
        self.student = Student(name, age)
        self.standard = standard
    def get_standard(self):
        return "%s's age is %s and belongs to %s category." % (self.student.name, self.student.age, self.standard)

b_student = Standard("Ravi", 28, "CSE")
print(b_student.get_standard())
