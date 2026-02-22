# lambda it is a small anonymous function
# it can take any number of arguements but just one expression 
# --- syntax --- 
# LAMBDA ARGUEMENTS : EXPRESSION

# ------ adding -----
# x = lambda a : a + 10
# print(x(5))

# ------ multiplying -----
# y = lambda a, b: a * b 
# print(y(5, 6))

# # ------ SUMMARIZING -----
# z = lambda a, b, c: a + b + c
# print(z(5, 6, 7))

# def myfunction(n):
#   return lambda a : a * n
# product = myfunction(2)
# print(product(11))

def myfunction(n):
  return lambda a : a * n
outcome = myfunction(3)
print(outcome(11))

# lambda is used to create small one time unamed function
def myfunction(n):
  return lambda a : a * n 
product = myfunction(2)
outcome = myfunction(3)
print(product(11))
print(outcome(11))