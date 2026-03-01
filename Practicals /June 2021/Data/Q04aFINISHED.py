# Q04(a)

import random

# Get input

productname = input("enter your product name: ")

# Generate a random number between 10 and 30 inclusive

randomnumber = random.randint(10,30)


# Generate the product code - first three letters of product name and the random number
productcode = productname[0:3] + str(randomnumber)



# Display the product code and the product name
print("Your product code is: " + productcode + " and the name of your product is: " + productname)


