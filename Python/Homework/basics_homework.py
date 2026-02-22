import math

# Question 1
x = 300
y = 330
if y > x:
    print('y is greater than x')
else:
    print('y is not greater than x')

# Question 2
name = input('What is your name? ')
age = input('What is your age? ')
height = input('What is your height? ')
weight = input('What is your weight? ')
print("Your details are:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Weight:", weight)

# Question 3
food = input('What is your favourite food? ')
name = input('What is your name? ')
print(name + ' likes ' + food)

# Question 4
name = input('What is your name? ')
age = input('What is your age? ')
school = input('What school do you go to? ')
print(name + ' is ' + age + ' and goes to ' + school + ' school')

# Question 5 (reverse order)
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print(last_name + ' ' + first_name)

# Question 6
n = input("Enter an integer: ")
result = int(n) + int(n*2) + int(n*3)
print("Result:", result)

# Question 7 (sphere volume)
radius = 6
volume = (4/3) * math.pi * radius**3
print("The volume of the sphere is:", volume)

# Question 8 (odd/even)
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
