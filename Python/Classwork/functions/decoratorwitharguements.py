def changecase(n):
  def changecase(func):
    def myinner():
      if n==1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase
@changecase(1)
def myfunction():
  return "HELLO WORLD"
print(myfunction())

# decorators can accept their own arguements by adding another level 