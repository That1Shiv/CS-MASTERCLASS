# a function is called with the correct number of arguemnts 
# eg if you expect two arguements you have to calll the function with two arguements not more not less 

# def myfunction(fname,lname):
#   print(fname + ' ' + lname)
  
# myfunction("shiv")

# ARBITRATRY ARGUEMENTS 
# if you do not know how many arguements will be passed into your function add a  star in the parameter
# def myfunction(*kids):
#   print("the youngest child is " + kids[2])

# myfunction("shiv","babu","shiven")


#keyword arguemnts 
# you can send arguements with the key = value syntax the order of the arguement does not matter
# def myfunction(child1, child3, child2):
#   print("the youngest child is " + child3)

# myfunction(child1 = "babu", child2 = "shiven", child3 = "shiv")


# arbitrary keyword arguements
# if you do not know how many keyword arguements are passed into the function add 2 stars before the parameter name in the function 
# def myfunction(**kids):
#   print("his last name is " + kids["lname"])

# myfunction(fname = "shiv", lname = "chauhan")




