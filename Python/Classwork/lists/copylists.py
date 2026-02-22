students = ["Alice", "Bob", "Charlie", "David", "Alice", "alex"]
integer_list = [42, 23, 16, 15, 8, 4] 

#copying the list using the list() operator 
new_list = list(students)
print(new_list) 

# copy using the slicing method
new_list_2 = students[:]
print(new_list_2)




# students.sort(key=str.lower)
# print(students)
# def myfunc(n):
#   return abs(n-23)
# integer_list = [42, 23, 16, 15, 8, 4] 
# integer_list.sort(key=myfunc)


# # words are sorted alphabetically 
# students.sort()



# # integers are sorted numerically from smallest to largest 
# integer_list.sort()



# students.sort(reverse=True)
