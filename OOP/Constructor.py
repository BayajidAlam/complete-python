class Student:
  def __init__(self):
    print("student object created")

stu = Student()


class NewStudent:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

student = NewStudent("John Doe", 20)

print(student.name)
print(student.age)