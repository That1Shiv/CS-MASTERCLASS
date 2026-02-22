# This is a nested if statement. It allows you to check conditions inside other conditions for more complex decision-making.
x = 30 
if x > 10: 
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
