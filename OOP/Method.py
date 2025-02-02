class NewStudent:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def SayHello(self):
        print("Hello, my name is " + self.name)

student = NewStudent("John Doe", 20)
student.SayHello()