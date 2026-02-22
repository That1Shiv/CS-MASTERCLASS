quantity = 3 
itemno = 5421
price = 124
myorder = "i want {1} pieces of item number {2} for {2:.2f} euros."
print(myorder.format(quantity, itemno, price))

age = 50
name = "osom"
txt = "his name is {1}. {1} is {0} years old"
print(txt.format(age, name))