# https://www.hackerrank.com/challenges/30-inheritance/problem
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
	"""
	Class Constructor
	  
	Parameters:
	firstName - A string denoting the Person's first name.
	lastName - A string denoting the Person's last name.
	id - An integer denoting the Person's ID number.
	scores - An array of integers denoting the Person's test scores.
	"""
	def __init__(self, firstName, lastName, idNumber, scores):
		Person.__init__(self, firstName, lastName, idNumber)
		self.scores = []
		for s in scores:
			self.scores.append(int(s))
	def calculate(self):
		"""
		Function Name: calculate
	    Return: A character denoting the grade.
	    """
		a = float(sum(self.scores))/len(self.scores)
		if a < 40:
			return 'T'
		elif a < 55:
			return 'D'
		elif a < 70:
			return 'P'
		elif a < 80:
			return 'A'
		elif a < 90:
			return 'E'
		else:
			return 'O'

if __name__ == '__main__':
	s = Student('Heraldo', 'Memelli', 8135627, [100.0, 80.0])
	s.printPerson()
	print("Grade: {:s}".format(s.calculate()))