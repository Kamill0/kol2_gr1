#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

#!/usr/bin/python
from subject import Subject
from student import Student
from diary import Diary

"""
sub1 = Subject("Matematyka", "prof. Kwiatkowski")
sub2 = Subject("J. polski", "prof. Nowak")
sub3 = Subject("Biologia", "prof. Kowalski")
sub4 = Subject("Historia", "prof. Kot") 
sub5 = Subject("WF", "prof. Szybki") 


stud1 = Student("Adam", "Abacki")
stud2 = Student("Bartosz", "Babacki")
stud3 = Student("Cezary", "Cabacki")
	
stud1.assign_classes([sub1, sub2, sub3])
stud2.assign_classes([sub1, sub2, sub3, sub4, sub5])
stud3.assign_classes([sub1, sub5])

stud1.assign_grades("Biologia", [3.0, 4.0, 5.0])
stud1.assign_grades("Matematyka", [2.5, 3.0, 4.5])

stud2.assign_grades("Historia", [3.0, 4.0, 5.0])
stud2.assign_grades("WF", [2.5, 3.0, 4.5])

stud3.assign_grades("Matematyka", [3.0, 4.0, 5.0])

diary = Diary("High school", "2016/2017")
diary.append_students([stud1, stud2, stud3])
diary.print_students()

diary.get_student("Adam", "Abacki").compute_total_average().compute_subject_average("Biologia").increment_attendance("Biologia", 5).print_attendance()
"""

diary = Diary("High school", "2016/2017")
classes = []
ans = True
ans2 = True
while ans:
	print("""
	1. Add a student
	2. Add a subject
	3. Print students
	4. Select student
	5. Exit 
	""")
	ans=raw_input("What would You like to do? ")
	if ans=="1":
		print("Adding a student:\n")
		first_name=raw_input("Enter first name: ")
		last_name=raw_input("Enter last name: ")
		if first_name.isalpha() and last_name.isalpha():
			stud = Student(first_name, last_name)
			diary.append_students([stud])
			print("Successfully added!\n")
		else:
			print("First name and last name must consist of letters only!\n")
	elif ans=="2":
		print("Adding a subject:\n")
		name=raw_input("Enter subject name: ")
		teacher_name=raw_input("Enter teacher name: ")
		if name.isalpha() and teacher_name.isalpha():
			sub = Subject(name, teacher_name)
			classes.append(sub)
			print("Successfully added!\n")
		else:
			print("Subject name and teacher name must consist of letters only!\n")	
	elif ans=="3":
		diary.print_students()
	elif ans=="4":
		print("Select a student:\n")
		first_name=raw_input("Enter first name: ")
		last_name=raw_input("Enter last name: ")
		if first_name.isalpha() and last_name.isalpha():
			stud = diary.get_student(first_name, last_name)
			if stud:
				ans2=True
				while ans2:
					print("""
					1. Assign classes
					2. Assign grades
					3. Compute total average
					4. Compute subjects average
					5. Increment attendance
					6. Print classes
					7. Print grades
					8. Print attendance 
					9. Return to previous menu
					""")
					ans2=raw_input("What would You like to do? ")
					if ans2=="1":
						stud.assign_classes(classes)
						print("Successfully assigned!\n")
					elif ans2=="2":
						example_grades = [2.5, 3.0, 4.0, 3.5]
						name=raw_input("Enter subject name: ")
						stud.assign_grades(name, example_grades)
					elif ans2=="3":
						stud.compute_total_average()
					elif ans2=="4":
						name=raw_input("Enter subject name: ")
						stud.compute_subject_average(name)
					elif ans2=="5":
						name=raw_input("Enter subject name: ")
						stud.increment_attendance(name)
					elif ans2=="6":
						stud.print_classes()
					elif ans2=="7":
						stud.print_grades()					
					elif ans2=="8":
						stud.print_attendance()
					elif ans2=="9":
						break
					else:
						print("No such option\n")
					
		else:
			print("First name and last name must consist of letters only!\n")
	elif ans=="5":
		break
	else:		
		print("No such option\n")			 			
	




