students = ["Alice", "Bob", "Charlie", "David", "Alice", "alex"]
integer_list = [42, 23, 16, 15, 8, 4] 


students.sort(key=str.lower)
print(students)
def myfunc(n):
  return abs(n-23)
integer_list = [42, 23, 16, 15, 8, 4] 
integer_list.sort(key=myfunc)
# print(integer_list)

# words are sorted alphabetically 
students.sort()
# print(students)


# integers are sorted numerically from smallest to largest 
integer_list.sort()
# print(integer_list)


students.sort(reverse=True)
# print(students)
