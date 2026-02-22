# tuples are unchangeable 
# to update convert into a list 
# After updating convert back to a tuple 
# tuples can be deleted entirely but not directly changeable (you have to convert to list) ( you can use .del)

fruits_tuple = ("apple", "banana", "cherry")
fruits_list = list(fruits_tuple)
fruits_list[1] = "kiwi"
fruits_tuple = tuple(fruits_list)
c = ('pineapple',)
fruits_tuple += c 
# print(fruits_tuple) 

# remove apple from the fruits tuple 
a = list(fruits_tuple)
a.remove('apple') 
fruits_tuple = tuple(a) 
print(fruits_tuple) 
