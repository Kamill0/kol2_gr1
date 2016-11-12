class Subject(object):
	"""Class represents a single school subject"""
	def __init__(self, name, data):
		"""Default init method"""		
		self.name = name
		self.grades = data[0]
		self.attendance = data[1]
		
	def get_average(self):
		"""Returns average grade of a subject"""
		return sum(self.grades)/float(len(self.grades))

	def get_attendance(self):
		"""Returns percentage attendance of a subject"""
		return sum(self.attendance)/float(len(self.attendance)) * 100.
		
	"""Getter & setter methods"""
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@property
	def grades(self):
		return self.__grades

	@grades.setter
	def grades(self, grades):
		self.__grades = grades

	@property
	def attendance(self):
		return self.__attendance

	@attendance.setter
	def attendance(self, attendance):
		self.__attendance = attendance


