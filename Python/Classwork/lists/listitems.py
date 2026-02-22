# list is a collection of data which is stored in a memory, 

teachers_list = ["tom", "babu", "florence", "rina"]
student_list = ["shiv", "jay", "saad", "shiven", "Shiven","Ken"]
fruits_list = ["apple","mange","banana","orange","strawberry"]
Schools_list = {"arya","Cg","samaj","Stmaries"}
colors_list = ["orange","yellow","blue","white","colorless","colorful"]
evennumbers_list = ["2",'4','6','8'] 

# Use the len() function to get the number of items in a list 
# List items are indexed 
# type() function is used to get the data type of a list 
# lists are defined as objects of the data type 'list' 
# list function is used to create a new list 

workers_list = list(('joash','isaac','unis'))
# you can use a list constructor to create a list 
# use index numbers to access the item list 
# negative indexing is starting from the end of the list
print(teachers_list[-1]) 

print(fruits_list[2:5])
# it will return the third, fourth and fifth items 
print(fruits_list[:5])
# returns all values from the beginning to the fifth 
print(fruits_list[2:])
# returns all items from the 2nd index until the end of the list 
print(fruits_list[-4:-1])
#returns all items except from the first and last item 
