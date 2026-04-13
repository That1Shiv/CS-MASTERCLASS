# Q04c

# import libraries
import random

# program constants
SIDES = 6
THROWS = 3

# complete the lines to initialise the variables
roll = 0 
subtotal = 0
booster = 1 
finalScore = 0

# roll dice 3 times
for throw in range(THROWS):
    # display number rolled
    roll = random.randint(1, SIDES)
    print("Rolled: ", roll)
    
    # update subtotal
    subtotal = subtotal + roll 
    
    # check for roll of 3 or 6 and increment booster if needed
    if roll == 6 or roll ==  3: 
        booster +=  1 
    
# calculate and output final score
finalScore = subtotal + booster
print("Final score: ", finalScore)