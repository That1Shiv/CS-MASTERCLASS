# decorators add extra behaviour to a function without changing the functions code 
# a decortor is a function that takes another function as a input and returns a new function 

def changecase(func):
  def myinner():
    return func().upper()
  return myinner
@changecase
def myfunction():
  return "hello world"
@changecase
def otherfunction(): # you can have multiple decorators 
  return "hello everyone"
print(myfunction())
print(otherfunction())

# by placing a @changecase  directly above the function definition the function is being decorated in the change case function 
# the function @changecase is the decorator 
