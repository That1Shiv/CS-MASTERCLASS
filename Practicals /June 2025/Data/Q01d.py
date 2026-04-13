# Q01d

# program variables
sales = 0.0
age = 0

def getWages(inSales, inAge):
    wages = 0
    if inSales > 2000 and inAge >= 21:
        wages = 1000 + (inSales * 0.05) # add 5% commission
    else:
        wages = 1000
    
    return wages

sales = float(input("please enter this month's sales: £"))
age = int(input("please enter age: "))

print("Wages: £", getWages(sales, age))