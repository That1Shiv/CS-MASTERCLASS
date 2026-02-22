# tuples are unchangeable 
# to update convert into a list 
# After updating convert back to a tuple 


fruits_tuple = ("apple", "banana", "cherry")
fruits_list = list(fruits_tuple)
fruits_list[1] = "kiwi"
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
