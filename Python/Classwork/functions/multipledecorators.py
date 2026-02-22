def changecase(func): 
  def myinner(): 
    return func().upper()
  return myinner 
def addgreeting(func):
  def myinner(): 
    return "hello " + func() + "!"
  return myinner
@changecase 
@addgreeting  
def myfunction():
  return "shiv" 
print(myfunction())