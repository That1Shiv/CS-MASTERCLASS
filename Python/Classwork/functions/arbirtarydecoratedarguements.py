def changecase(func):
  def myinner(*agrs, **kwargs):
    return func(*agrs, **kwargs).upper()
  return myinner
@changecase
def myfunction(a):
  return "bye" + a
print(myfunction(" babu"))
