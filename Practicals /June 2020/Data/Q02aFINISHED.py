#	Q2a

#	Initialise variables
base = 50 
heightChk = True 


#	Print prompt and take input from user
while heightChk: 
  height = int(input("Enter the height (between 1 and 100): "))
  if ( height >= 1 and height <= 100): 
    heightChk = False

#	Calculate area and print out value 

area = 0.5 * base * height 
print("Base of the triangle is:", base)
print("Height of the triangle is:", height)
print("Area of triangle is:", area)


