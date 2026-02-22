teachers = {"babu", "charles", "david", "Rina", 1, 2, 0}
male = {"babu", "tom", "obi", 1, 2, 0}

staff_3 = teachers.symmetric_difference(male)
print(staff_3) 

staff_2 = teachers ^ male
# print(staff_2)

staff = teachers - male
# print(staff) 


Sch = teachers.intersection(male)
# print(Sch)




school = teachers.difference(male)
# print(school) 







staff = teachers.intersection(male)
# print(staff)

tutors = teachers&male 
# print(tutors)

teachers.intersection_update(male)
# print(teachers)  

