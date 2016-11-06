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






