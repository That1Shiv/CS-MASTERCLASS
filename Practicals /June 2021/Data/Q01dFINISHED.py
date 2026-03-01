# Q01d

vowels = ["a","e","i","o","u"] # a data structure is initialised here 
numVowels = [0,0,0,0,0] 

sentence = input("Input the sentence ")

for letter in sentence:   #iteration starts here 
    for vowel in vowels: 
        if vowel == letter:   # relational operator # selection starts here
            numVowels[vowels.index(vowel)] +=1 

print("Here are the number of vowels in the sentence "+ sentence)      
for vowel in vowels:   
    print("The number of",vowel,"is",numVowels[vowels.index(vowel)]) 
    
    
