# Q02cii

# program CONSTANTS
HEXDIV = 16

# program variables
userInput = 0

# subprogram to get hex letter
def getLetter(hexDigit):
    hexLetter = ""
    if hexDigit == 10:
        hexLetter = "A"
    elif hexDigit == 11:
        hexLetter = "B"
    elif hexDigit == 2:
        hexLetter = "C"
    elif hexDigit == 13:
        hexLetter = "D"
    elif hexDigit == 14:
        hexLetter = "E"
    elif hexDigit == 15:
        hexLetter = "F"
    else:
        hexLetter=str(hexDigit)
    return hexLetter

# subprogram to create 8-bit binary value
def getHex(denaryValue):
    hexResult = ""
    hexFirst = denaryValue // HEXDIV
    hexSecond = denaryValue % HEXDIV
    hexResult = getLetter(hexFirst) + getLetter(hexSecond)
    return hexResult

# complete the line to convert the user input to integer
userInput = int(input("please enter a number between 0 and 255 \n"))

# complete the test to check the input is between 0 and 255
if (userInput >= 0) and (userInput <= 256):
    # complete the line to call getHex subprogram
    print(getHex(userInput))
else:
    print("number out of range")