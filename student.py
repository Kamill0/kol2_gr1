from subject import Subject

class Student(object):
	"""Class represents a single student"""
	def __init__(self, name, subjects):
		"""Default init method"""
		self.name = name
		self.subjects = subjects

	def __str__(self):
		"""To string method"""
        	return self.name
				
	def compute_subject_average(self, subject):
		"""Computes average grade of a specific subject"""
		sub = next((s for s in self.subjects if s.name == subject), None)
		if sub:
			return sub.get_average()		
	
	def compute_total_average(self):
		return sum([subject.get_average() for subject in self.subjects])/float(len(self.subjects))

	def compute_subject_attendance(self, subject):
		"""Computes average grade of a specific subject"""
		sub = next((s for s in self.subjects if s.name == subject), None)
		if sub:
			return sub.get_attendance()		
	
	def compute_total_attendance(self):
		return sum([subject.get_attendance() for subject in self.subjects])/float(len(self.subjects))

	
	"""Getter & setter methods"""
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name =  name

	@property
	def subjects(self):
		return self.__subjects

	@subjects.setter
	def subjects(self, subjects):
		self.__subjects =  subjects

