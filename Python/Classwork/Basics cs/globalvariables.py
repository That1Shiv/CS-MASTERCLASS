# global variables are created outside the function and can be used in any function
# local variables are created inside a function and can only be used inside the function except when converted to global 


#global variable
a = 'how are you?'
def myfunc():
  print('babu is asking  ' + a) 
myfunc()

