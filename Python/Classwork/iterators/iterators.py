# iterator is a object that contains a countable number of values 
# In python an iterator is a object which implements the iterator protocal which consist of methods __iter__() and __next__()
 
# return a iterator from a tuple and print each value 


# EG 1 
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# strings are also iterable objects 

mystr = "babu"
myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# looping an iterator 
for x in mytuple:
  print(x) 


