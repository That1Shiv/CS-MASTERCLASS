# Q02a

# Initialise variables
username = "bard423"
password = "nX2934?"
count = 0 
# Print prompts, take and check input from user
while True: 
  usersinput_username = input("Please enter your username: ")
  usersinput_password = input("Please enter your password: ")
  if usersinput_username == username and usersinput_password == password: 
    print("Welcome")
    break 
  else: 
    print("please try again")
    count += 1 