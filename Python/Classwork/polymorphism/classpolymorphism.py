# ------- class polymorphism ------------ 
# many classes with the same method name 
class car: 
  def __init__(self, brand, model): 
    self.brand = brand 
    self.model = model 
  def move(self): 
    print("car is moving") 

class boat: 
  def __init__(self, brand, model): 
    self.brand = brand 
    self.model = model 
  def move(self): 
    print("boat is sailing")

class plane: 
  def __init__(self, brand, model): 
    self.brand = brand
    self.model = model 
  def move(self): 
    print("plane is flying")  

# create a car object
car1 = car("BMW", "x5")


# create a boat object
boat1 = boat("Yamaha", "001")

# create a plane object
plane1 = plane("boeing", "747")

for x in (car1, boat1, plane1): 
  x.move()