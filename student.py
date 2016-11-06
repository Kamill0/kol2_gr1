from subject import Subject

class Student(object):
	"""Class represents a single student"""
	def __init__(self, first_name, last_name):
		"""Default init method"""
		self.first_name = first_name
		self.last_name = last_name
		self.classes = []
		self.grades = {}
		self.attendance = {}

	def __str__(self):
		"""To string method"""
        	return self.first_name + " " + self.last_name

	def assign_classes(self, classes):
		"""Assigns a list of classes to the specific student.
		In case he already has some, the new one will be appended
		"""
		if not isinstance(classes, list):
			print("Pass the classes as a list object!!!")
			return
		
		for i in classes:
			if not isinstance(i, Subject):
				print("Incompatible types - You must provide a valid Subject object")
				return
		self.classes.extend(classes)
		for i in self.classes:
			self.attendance[i.name] = 0

	def __check_subject_existance(self, subject):
		"""Helper method used internally to determine if student has the passed subject already assigned"""
		sub_exists = False
		for i in self.classes:
			if subject == i.name:
				sub_exists = True
		return sub_exists


	def assign_grades(self, subject, grades):
		"""Assigns a set of grades to specific subject"""
		if not isinstance(grades, list):
			print("Pass the grades as a list object!!!")
			return

		sub_exists = self.__check_subject_existance(subject)
		if sub_exists:
			if subject in self.grades.keys():
				self.grades[subject].extend(grades)
			else:
				self.grades[subject] = grades
		else:
			print("No such subject: " + subject + ".\nPick one from below\n")
			self.print_classes()
			return

	def increment_attendance(self, subject, value = 1):
		"""Increments attendance on a given subject by specified value (0 by default)"""
		sub_exists = self.__check_subject_existance(subject)
		if sub_exists:
			if subject in self.attendance.keys():
				self.attendance[subject] += value
			else:
				self.attendance[subject] = value
		else:
			print("No such subject: " + subject + ".\nPick one from below\n")
			self.print_classes()
		return self
				
	def compute_subject_average(self, subject):
		"""Computes average grade of a specific subject"""
		sub_avg = 0.
		counter = 0
		sub_exists = self.__check_subject_existance(subject)
		if sub_exists:
			for y in self.grades[subject]:
				sub_avg += y
				counter += 1
			print("Average (" + subject + ") is: " + str(sub_avg/counter))	
		else:
			print("No such subject: " + subject + ".\nPick one from below\n")
			self.print_classes()
		return self
	
	def compute_total_average(self):
		"""Computes average grade of all student's subjects"""
		total_avg = 0.
		counter = 0

		for x in self.grades:
			for y in self.grades[x]:
				total_avg += y
				counter += 1
		if counter!= 0:
			print("Average (total) is: " + str(total_avg/counter))	
		return self
	
	def print_classes(self):
		"""Prints student's classes"""
		print("Subject list:")
		print("\n".join(str(p) for p in self.classes))
		return self 

	def print_grades(self):
		"""Prints student's grades"""
		print("\nGrades of:")
		print(self)
		for i in self.grades:
			print(i + ": ")
			for y in self.grades[i]:
				print(y)
		return self
	def print_attendance(self):
		"""Prints student's attendance"""
		print("\nAttendance:")
		for i in self.attendance:
			print(i + ": " + str(self.attendance[i]))
		return self
	
	"""Getter & setter methods"""
	@property
	def first_name(self):
		return self.__first_name

	@first_name.setter
	def first_name(self, first_name):
		self.__first_name = first_name

	@property
	def last_name(self):
		return self.__last_name

	@last_name.setter
	def last_name(self, last_name):
		self.__last_name = last_name
