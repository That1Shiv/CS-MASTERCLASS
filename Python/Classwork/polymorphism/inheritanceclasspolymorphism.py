# ------- inheritance class polymorphism ---------------- 
class vehicle: 
  def __init__(self, brand, model): 
    self.brand = brand 
    self.model = model 
  def move(self): 
    print("vehicle is moving")

class car(vehicle):
  pass  

class boat(vehicle): 
  def move(self): 
    print("boat is sailing fast")

class plane(vehicle): 
  def move(self): 
    print("plane is flying high")

car1 = car("mazda", "cx5")
boat1 = boat("yamaha", "002")
plane1 = plane("airbus", "B678")

for x in (car1, boat1, plane1): 
  print(x.brand,)
  print(x.model)
  x.move()
