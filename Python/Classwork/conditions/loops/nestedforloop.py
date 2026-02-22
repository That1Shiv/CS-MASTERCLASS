# This is a nested for loop. It allows you to iterate over multiple sequences, combining their elements in every possible way.
list = [1, 2, 3, 4, 5]
list1 = ["apple", "banana", "cherry", "orange", "kiwi"]
for x in list:
    for y in list1:
        print(x, y)
