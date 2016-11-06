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

stud1 = Student("Kamil", "Potoczny")
sub_list = [sub1, sub2, sub3]
stud1.assign_classes(sub_list)

stud1.assign_grades("Biologia", [3.0, 4.0, 5.0])
stud1.assign_grades("Kappa", [3.0, 4.0, 5.0])

stud1.print_grades()
stud1.compute_subject_average("Biologia")
stud1.compute_total_average()




