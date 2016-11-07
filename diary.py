from subject import Subject
from student import Student

class Diary(object):
	"""Class represents a school diary"""
	def __init__(self, school_name, year, students = []):
		"""Default init method"""
		self.school_name = school_name
		self.year = year			
		self.students = students

	def __str__(self):
		"""To string method"""
        	return self.school_name + ", year of: " + self.year + "\n"

	def append_students(self, students):
		"""Appends students list to the diary"""
		if not isinstance(students, list):
			print("Pass the students as a list object!!!")
			return		
		
		for i in students:
			if not isinstance(i, Student):
				print("Incompatible types - You must provide a valid Student object")
				return
		self.students.extend(students)

	def get_student(self, first_name, last_name):
		"""Returns specific student"""
		for i in self.students:
			if i.first_name == first_name and i.last_name == last_name:
				print("\nSelected student:")
				print(i)
				return i
		print("No matching student")
		return

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
