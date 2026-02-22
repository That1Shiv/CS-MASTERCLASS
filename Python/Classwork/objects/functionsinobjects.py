class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 

  def myfunc(self):
    print("good evening " + self.name)

p1 = Person("ochami", 36)
p1.myfunc()
p1 = Person("ochami", 36)
p1.myfunc()

