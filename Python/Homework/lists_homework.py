# List theory
# 1. Lists are ordered collections of items.
# 2. Lists can contain different data types.
# 3. Lists are mutable (can be changed).
# 4. Lists can be nested.

# Example lists
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry']
mixed = [10, 'hello', 3.14, True, None]

# Question tasks
List1 = [10, 20, 30, 40, 50]
List2 = [60, 70, 80, 60]

# a. Check if 12 not in List1
if 12 not in List1:
    print("List1 does not contain 12.")

# b. Concatenate
List3 = List1 + List2
print("Concatenated List:", List3)

# c. Repeat
List4 = List1 * 5
print("Repeated List1:", List4)

# d. Index access
print("Item at index 3 in List1:", List1[3])
print("Item at index 3 in List2:", List2[3])

# e. Count
print("Total items in List1:", len(List1))
print("Total items in List2:", len(List2))

# f. Remove first occurrence of 40
List1.remove(40)
print("List1 after removing 40:", List1)

# g. Modify item at index 2
List1[2] = 35
print("List1 after modifying index 2:", List1)

# h. Pop at index 2
removed_item = List1.pop(2)
print("Removed:", removed_item)

# i. Append nested list
List1.append([2, 5, 7])
print("List1 after appending:", List1)

# j. Max and Min
print("Max item:", max(List2))
print("Min item:", min(List2))

# k. Check if 80 not in lists
if 80 not in List1:
    print("List1 does not contain 80.")
if 80 not in List2:
    print("List2 does not contain 80.")

# l. Copy
List2 = List1.copy()
print("Copied List2:", List2)

# Functions
def reverse_list_at_index(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[:index] + lst[index:][::-1]

def find_biggest(lst):
    return max(lst) if lst else "List is empty"

def first_non_repeated(lst):
    for item in lst:
        if lst.count(item) == 1:
            return item
    return None

def sum_of_list(lst):
    return sum(lst)

def find_smallest(lst):
    return min(lst) if lst else "List is empty"

def is_list_empty(lst):
    return len(lst) == 0

def append_lists(a, b):
    a.extend(b)
    return a

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result
