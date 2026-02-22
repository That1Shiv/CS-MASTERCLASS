# This for loop breaks before printing when a condition is met, so the value is not printed if the condition is true.
list = [1, 2, 3, 4, 5]
for x in list: 
    if x == 3:
        break
    print(x)
