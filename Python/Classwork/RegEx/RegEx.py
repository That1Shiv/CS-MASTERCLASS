# Used to check if a string contains specified search patterns 
# the inbuilt module is known as re
 
import re 
txt = "Hi i am going to write my notes after studying python"
x = re.search("^Hi.*python$",txt)
print(x)

