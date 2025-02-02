class Father:
  def show_father(self):
    print("Father property")

class Mother:
  def show_mother(self):
    print("Mother property")

class Child(Father, Mother):
  def show_child(self):
    print("Child property")

child = Child()
child.show_father()
child.show_mother()
child.show_child()