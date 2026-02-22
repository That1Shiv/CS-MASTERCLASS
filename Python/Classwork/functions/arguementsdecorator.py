def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner
@changecase
def myfunction(y):
  return "hello" + y
print(myfunction(" shiv"))
