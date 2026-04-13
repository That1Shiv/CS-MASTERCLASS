# Q01bii

# initialise counters
ballCount = 0
greenCount = 0
redCount = 0

ballArray = ["green", "red", "green", "green", "red", "green","green", "green",
             "green", "green", "green", "red", "green", "red", "green", "red",
             "red", "green", "green", "red", "red", "green", "green", "red",
             "green", "red", "red", "green", "green", "red", "green", "green",
             "red", "green", "green", "green", "red", "green", "red","green"]

# iterate over ball array
for ball in ballArray:
    ballCount = ballCount + 1
    if ball == "green":
        greenCount = greenCount +1
    else:
        redCount = redCount + 1
        
print(" Green: ", greenCount, "balls \n", "Red: ", redCount,
      "balls \n", "Total: ", ballCount, "balls")