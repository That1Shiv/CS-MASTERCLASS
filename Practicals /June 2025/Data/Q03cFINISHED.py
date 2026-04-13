# Q03c

# program variables


# ----------------------------------------------
# Write your code below this line
age = 0 
count = 0
total = 0 

age = int(input("Please enter your age: "))

while age != 0: 
  total += age 
  count += 1 
  
  age = int(input("Please enter your age in years: "))
  
if count == 0: 
  print("No ages input")
else: 
  average = int(total/count)
  print("you entered", count, "ages; the average is", average)
  