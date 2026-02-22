class person: 
  def __init__(self, fname, lname): 
    self.firstname = fname 
    self.lastname = lname 
  def printname(self): 
    print(self.firstname, self.lastname)


class student(person):
  def __init__(self, fname, lname, year): 
    super().__init__ (fname, lname)
    self.graduationyear = year
  def greet(self): 
    print("hi", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = student("babu", "balu", 2025)
x.greet()
      