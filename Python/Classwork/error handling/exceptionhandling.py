# try is for testing a block of code for errors 
# except is for handling the error
# else is for executing the code when there is no error 
# finally is for executing the code regardless of try and except (whether the code works or not)


# ----------- exception handling -------------
try: 
  print(x)
except: 
  print("an exception occured")



# -------------- Many exceptions --------------
try: 
  print(x)
except NameError: 
  print("variable x is not defined")
except: 
  print("something else went wrong")
  
  
# --------------- else keyword -------------
try: 
  print("hello")
except: 
  print("Something went wrong")
else:
  print("nothing went wrong")
  
  

  
# ------------ finally keyword --------------
try: 
  print(x)
except: 
  print("Something went wrong")
finally:
  print("The try except is finished")
  

