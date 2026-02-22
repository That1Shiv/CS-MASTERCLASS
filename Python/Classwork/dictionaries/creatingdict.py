cars1 = {
  "bmw": "Germany",
  "ford": "USA",
  "honda": "Japan",
  "bmw": "kenya"
}
# print(cars1)

# print(len(cars1))

# the len function returns the number of items  
# print(len(cars1))

# duplicate values overwrite exsisting values
# print(type(cars1))



boy = dict(name = "tom", age = "15", country = "kenya")
# print(boy)

x = boy["age"]
# print(x)

y = boy.keys()
# print(y)


# adding item to dictionary 
boy["height"] = "5feet"
# print(boy) 


# creating notes of the key and value pairs 
# z = boy.items()
# print(z)

boy["name"] = "thomas"
# print(boy) 

# if "name" in boy:
  # print("yes, 'name' is one of the keys in the dictionary")

# using the update method to change the value of a key
boy.update({"name": "james"})
# print(boy)



# boy.pop("age")
# print(boy)

boy.popitem()

# del boy ["name"]
# print(boy)

# del boy

# cars1.clear()
# print(cars1)

