#	Q02b

#	Set initial values of variables



# 	Request input
Length = int(input("Enter the length: "))
Width = int(input("Enter the width: "))


# 	Calculate number of panels needed

panels = (2 * Length ) + ( 2 * Width) - 4 

# 	Print out number of panels needed
print("Number of panels needed: ", panels)
