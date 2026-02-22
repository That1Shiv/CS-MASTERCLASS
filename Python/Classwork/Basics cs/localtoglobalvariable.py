b = 'easy'

def myfunc():
  b = 'very easy'
  print('programming with python is  ' + b)
myfunc()

def func():
  global b
func()
print('programming with python is  ' + b)

