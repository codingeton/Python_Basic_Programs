#A simple program to demonstrate inheritance in Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def basic_details(self):
        return "%s's age is %s." % (self.name, self.age)

class Standard(Student):
    def __init__(self, name, age, standard):
        Student.__init__(self, name, age)
        self.standard = standard

    def get_standard(self):
        return "%s's age is %s and belongs to %s standard." % (self.name, self.age, self.standard)

if __name__ == 'main':
    first_student = Student("Ravi", 28)
    print(first_student.basic_details())
    second_student = Standard("Teja", 27, "B.tech")
    print(second_student.get_standard())
