from subject import Subject
from student import Student
from pprint import pprint
import re
import json

class Diary(object):
	MENU = ["\n************Main Menu************\n1. Add a student\n2. Delete student\n3. Display all students\n4. Select student\n5. Exit\nWhat would You like to do? ", "\n************Student Menu************\n1. Get total average\n2. Get subject average\n3. Get total attendance\n4. Get subject attendance\n5. Return\nWhat would You like to do? ", "\n*********************************\n"]

	"""Class represents a school diary"""
	def __init__(self, school_name, year, filename):
		"""Default init method"""
		self.school_name = school_name
		self.year = year
		self.filename = filename
		self.json_data = {}
		self.students = self.__load_data(self.filename)		

	def __load_data(self, filename):
		"""Loads data from JSON file"""
		with open(filename) as data_file:    
    			self.json_data = json.load(data_file)
		return [Student(stud, [Subject(sub, [y for x,y in self.json_data[stud][sub].iteritems()]) for sub in self.json_data[stud].keys()]) for stud in self.json_data.keys()]

	def __str__(self):
		"""To string method"""
        	return self.school_name + ", year of: " + self.year + "\n"

	def __save_and_update(self):
		"""Saves new JSON content and refreshes students entity"""
		json.dump(self.json_data, open(self.filename,"w"))
		self.students = self.__load_data(self.filename)

	def add_student(self):
		"""Adds a student to the JSON file"""
		new_subjects = {}
		stud_name = raw_input("Enter name: ")

		print("\nAdding subjects:\n")
		while True:
			sub_name = raw_input("Enter subject's name: ")
			new_grades = [float(i) for i in raw_input("Enter grades separated by space: ").split()]
			new_attendance = [int(i) for i in raw_input("Enter attendance separated by space: ").split()]
			new_subject = { sub_name : {"grades" : new_grades, "attendance" : new_attendance}}
			new_subjects.update(new_subject)

			if raw_input("Do You want to add another one [Y/N]? ") == "N":
				break		
		self.json_data.update({stud_name : new_subjects})
		self.__save_and_update()

	def delete_student(self):
		"""Deletes student"""
		try:		
			del self.json_data[raw_input("Enter student's name: ")]
			self.__save_and_update()
		except KeyError, e:
    			print("No matching student\n")

	def open_menu(self):
		"""Opens control menu"""
		current_student = None
		while True:
			ans=raw_input(self.MENU[0])
			print(self.MENU[2])
			if ans=="1":
				self.add_student()
			elif ans=="2":
				self.delete_student()
			elif ans=="3":
				self.print_students()
			elif ans=="4":
				current_student = self.get_student(raw_input("Enter student's name: "))
				if current_student:
					print(current_student)
					while True:
						ans=raw_input(self.MENU[1])
						print(self.MENU[2])
						if ans=="1":
							print(current_student.compute_total_average())
						elif ans=="2":
							print(current_student.compute_subject_average(raw_input("Enter subject's name: ")))
						elif ans=="3":
							print(str(current_student.compute_total_attendance()) + " %") 
						elif ans=="4":
							print(str(current_student.compute_subject_attendance(raw_input("Enter subject's name: "))) + " %")
						elif ans=="5":
							break
						else:
							print("No such option\n")
				else:
					print("No matching student")
			elif ans=="5":
				print("Goodbye!")
				break
			else:
				print("No such option\n")
		
	def get_student(self, student):
		"""Returns student"""
		return next((s for s in self.students if s.name == student), None)

	def print_students(self):
		"""Prints students"""
		print("Students list:")
		print("\n".join(str(p) for p in self.students)) 

	"""Getter & setter methods"""
	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, year):
		self.__year = year	

	@property
	def school_name(self):
		return self.__school_name

	@school_name.setter
	def school_name(self, school_name):
		self.__school_name = school_name


if __name__ == "__main__":
	diary = Diary("High school", "2016/2017", "data.json")
	diary.open_menu()		
