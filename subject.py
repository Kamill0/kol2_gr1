class Subject(object):
	"""Class represents a single school subject"""
	def __init__(self, name, teacher_name):
		"""Default init method"""		
		self.name = name
		self.teacher_name = teacher_name

	def __str__(self):
		"""To string method"""		
        	return self.name + " (" + self.teacher_name + ")"
		
	"""Getter & setter methods"""
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@property
	def teacher_name(self):
		return self.__teacher_name

	@teacher_name.setter
	def teacher_name(self, teacher_name):
		self.__teacher_name = teacher_name



