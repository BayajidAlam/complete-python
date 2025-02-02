class Animal:
  @staticmethod
  def make_sound():
    print("Some sound")

class Dog(Animal):
  @staticmethod
  def bark():
    print("Bark")

dog = Dog()
dog.make_sound()
dog.bark()