# This for loop uses 'break' to exit early and 'else' to run code only if the loop wasn't broken.
for x in range(6): 
    if x == 3: 
        break
    print(x)
else: 
    print("finally finished")
