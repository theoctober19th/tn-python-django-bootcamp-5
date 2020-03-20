class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        
    def set_age(self, age):
        self.age = age

    def set_marks(self, marks):
        self.marks = marks

    def display(self):
        print("Name=", self.name)
        print("Roll Number=", self.roll_number)
        print("Marks=", self.marks)


student = Student("Bikalpa", 100)
student.set_age(21)
student.set_marks([10, 10, 32, 78, 43])
student.display()