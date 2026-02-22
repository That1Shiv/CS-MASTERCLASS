# This while loop uses 'else' to run code after the loop finishes normally, not by break.
i = 1
while i < 6:
    print(i)
    i += 1 
else:
    print("i is no longer less than 6")
