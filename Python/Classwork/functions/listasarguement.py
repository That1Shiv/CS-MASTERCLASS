# if you send a list as a  argument it will still  be as a list when it reaches the function 
def myfunction(food): 
  for x in food:
    print(x)

fruits = ['banana', 'mango', 'grapes']
myfunction(fruits)

# you can send any data type of a arguement in the function and it will be trated as the same data type inside the function 