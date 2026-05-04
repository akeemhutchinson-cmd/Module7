thisdict1 = {"c.101": "RM 515", "c.102": "RM 313", "c.103": "RM 111"}
print(thisdict1)

thisdict2 = {"c.101": "Prof Mob", "c.102": "Prof Tokiyuki", "c.103": "Prof Midoriya"}
print(thisdict2)

thisdict3 = {"c.101": "11a", "c.102": "6p", "c.103": "4a"}
print(thisdict3)

# User inputs course number
course_number = input("Enter a course number: ")
#Use input to pull values
print(thisdict1.get(course_number), thisdict2.get(course_number), thisdict3.get(course_number))