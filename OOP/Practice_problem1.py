class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def calculate_average(self):
      sum = 0
      for mark in self.marks:
        sum += mark
      return sum/3

    @staticmethod
    def hello_world():
      return "Hello World"

student = Student("John",[90,80,70])
print(student.calculate_average())
print(Student.hello_world())
