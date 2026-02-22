# Tuple exercises

# Create tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])          # Access 3rd element
print(len(my_tuple))        # Length
print(my_tuple * 3)         # Repeat

# Slice
numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13)
print(numbers[3:7])

# Reverse
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])

# Unpack
tuple2 = (10, 20, 30, 40)
a, b, c, d = tuple2
print(a, b, c, d)

# Tuple formatting
def format_tuple(tup):
    return "The tuple contains: " + ", ".join(map(str, tup))

# Convert tuple to string
def tuple_to_string(tup):
    return " ".join(map(str, tup))

# 4th from last
my_tuple = (1,2,3,4,5)
print(my_tuple[-4])

# Find repeated items
my_tuple = (1,2,3,4,5,1,2)
repeated = {x for x in my_tuple if my_tuple.count(x) > 1}
print(repeated)

# List → tuple
my_list = [1,2,3,4,5]
print(tuple(my_list))

# Shallow copy
tuple1 = (10, 20, 30, 40)
tuple2 = tuple1
print(tuple2)
