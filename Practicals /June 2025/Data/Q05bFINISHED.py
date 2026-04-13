# Q05b

Tbl_scores = [[45,42,43],[19,36,41],[48,48,48],[35,32,31],
           [18,22,26],[41,35,31],[15,19,12],[41,39,40],
           [27,25,22],[32,36,35],[37,36,37],[40,35,41]]

# ----------------------------------------------
# Write your code below this line

total = 0 
grade = " "

file = open("grades.txt", "w")

# iterating through the students 
for student in Tbl_scores: 
  lowest = 51 
  total = 0 



  # iterating through the students SCORES
  for scores in student:  
    total = total + scores
    if scores < lowest:
      lowest = scores 
      
      
     
  # remove the lowest score from the total
  total = total - lowest 
  
  
  
  
  # what score did the student get? 
  if total >= 80: 
    grade = "distinction"
  elif total >= 65: 
    grade = "merit"
  elif total >= 50:
    grade = "pass"
  else: 
    grade = "fail"
  
  # write the total and grade to the file
  file_record = str(total) + " " + grade + "\n"
  file.write(file_record)

# close the file 
file.close()
print("grade file has been created") 

