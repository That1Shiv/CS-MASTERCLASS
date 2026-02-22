students = ["Alice", "Bob", "Charlie", "David", "Alice", "alex"]
integer_list = [42, 23, 16, 15, 8, 4] 

students.extend(integer_list)
print(students)

for x in integer_list:
    students.append(x)
# print(students)

# joining using the + operator 
new_list_3 = students + integer_list
# print(new_list_3)