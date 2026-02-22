# This for loop uses 'continue' to skip printing the value when a condition is met, resuming with the next item.
list = [1, 2, 3, 4, 5]
for x in list:
    if x == 3: 
        continue
    print(x)
