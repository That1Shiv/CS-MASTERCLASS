#      Q05


def displayMenu():
     # Completed subprogram that displays the menu
    
    print("                  Menu                    ")
    print("------------------------------------------")
    print("[1] Add player name")
    print("[2] Play guess the capital city")
    print("[3] End game")
    print("------------------------------------------")


def getMenuChoice():
    # Completed subprogram that gets and validates the menu choice
    choices = [1,2,3]
    mChoice = 0
    
    # Menu choice is validated
    while mChoice not in choices:
        mChoice = int(input("Input your menu choice: "))


    # Valid menu option returned to the main menu
    return mChoice
     
def addPlayerName():
    # Add your code to:
    #   ensure a player name is input
    #   return the player name to the main menu
    username = " "
    while username == " ":
        username = input("please enter a user name: ")
    return username 







def guessCapital():
    # Partially completed subprogram to:
    #   display questions
    #   check guesses
    #   return final score
    
    # Arrays holding question numbers, countries and their capital cities
    questions = [1,2,3,4,5,6,7,8,9]
    countries = ["England","France","Spain","Italy","Germany","Scotland","Wales","United Arab Emirates","China"]
    capitals = ["London","Paris","Madrid","Rome","Berlin","Edinburgh","Cardiff","Abu Dhabi","Beijing"]


    questionCount = 1
    questionScore = 0


    # Add your code here
    while questionCount <= 5: # Changed to 5
        print("\nAvailable question numbers:", questions)
        choice = int(input("Pick a question number: "))
        
        if choice in questions:
            index = choice - 1 # Assuming choice matches the 1-based index
            guess = input(f"What is the capital of {countries[index]}? ").lower()
            
            if guess == capitals[index].lower():
                print("Well done!")
                questionScore += 1
            else:
                print(f"Incorrect. The capital is {capitals[index]}")
            
            questions.remove(choice)
            questionCount += 1 # Increment only on valid choice
        else:
            print("Invalid choice, try again.")
            
    return questionScore


menuChoice = 0
score = 0
playerName = ""


while menuChoice != 3:
    displayMenu()
    menuChoice = getMenuChoice()
    
    # Add your code to:
    #   call the relevant subprogram if the menu choice is 1 or 2
    #   display the player name and the score if the menu choice is 3
    if menuChoice == 1: 
        playerName = addPlayerName()
    elif menuChoice == 2: 
        score = guessCapital()
    else: 
        print("Player name: ", playerName)
        print("Score: ", score)
        
    
        
