# Q06

# city and temperature arrays
Tbl_city = ["Reggane", "Cairo", "New Delhi", "Muscat", "Athens", "Barcelona", "Havana", "Phoenix", "Brisbane"]
Tbl_temps = ["F103", "F82", "C34", "F95", "C29", "F79", "F84", "C35", "F77"]

# ----------------------------------------------
# write subprogam(s) below this line
# subprogram to convert Celsius to Fahrenheit
def celtofah(temp): 
  F = (temp * 1.8) + 32 
  F = int(round(F, 0))
  return F 



# subprogram to convert Fahrenheit to Celsius 
def fahtocel(temp): 
  C = (temp - 32) / 1.8 
  C = int(round(C, 0))
  return C 
# ----------------------------------------------
# Write your code below this line


# Variables 
total_cel = 0 
total_fah = 0  
length_city = len(Tbl_city)

# Updating the temperature for each city 

Current_city = input("Please enter the name of a city: ")
for i in range(length_city): 
  if Current_city == Tbl_city[i]: 
    Current_temperature = input("please enter the temperature in the correct format: ")
    Tbl_temps[i] = Current_temperature
    break
else: 
  print("City not found in the list") 
  
  
  
# Display header 
layout = "{:16} {:^10} {:^10}"
print(layout.format("city", "Celsius", "Fahrenheit"))
print("_"*40)




# take each city and the temperature 
for i in range(length_city):
  next_temp = Tbl_temps[i]
  scale = next_temp[0]
  thetemp = int(next_temp[1:])
  
  
  
  
  # convert the temperature to the other scale 
  if scale == "C": 
    ctemp = thetemp
    total_cel += ctemp 
    ftemp = celtofah(thetemp)
    total_fah = total_fah + ftemp
  else: 
    ftemp = thetemp
    total_fah += ftemp 
    ctemp = fahtocel(thetemp)
    total_cel += ctemp
    
    
    
    
  # display the city and the temperatures 
  print(layout.format(Tbl_city[i], ctemp, ftemp))



# Calculate averages 
average_cel = int(round(total_cel / length_city , 0))
average_fah = int(round(total_fah / length_city , 0))



# table footer 
print("_"*40)
print(layout.format("average", average_cel, average_fah))

