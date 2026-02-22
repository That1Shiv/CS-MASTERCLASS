# Set exercises

# Create set
my_set = {1,2,3,4,5}
print(my_set)

# Iterate
for item in my_set:
    print(item)

# Add
my_set.add(6)
my_set.update([7,8])
print(my_set)

# Remove
my_set.remove(5)
my_set.discard(4)
print(my_set)

# Remove if present
if 3 in my_set:
    my_set.remove(3)
print(my_set)

# Union
my_set2 = {4,5,6}
union_set = my_set | my_set2
print(union_set)
