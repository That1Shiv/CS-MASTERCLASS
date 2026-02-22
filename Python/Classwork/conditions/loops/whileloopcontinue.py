# This while loop uses 'continue' to skip the current iteration when a condition is met, resuming with the next iteration.
i = 0 
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
