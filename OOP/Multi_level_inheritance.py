class Animal:
  @staticmethod
  def make_sound():
    print("Some sound")

class Dog(Animal):
  @staticmethod
  def bark():
    print("Bark")

class Puppy(Dog):
  @staticmethod
  def weep():
    print("Weep")

puppy = Puppy()

puppy.make_sound()
puppy.bark()
puppy.weep()