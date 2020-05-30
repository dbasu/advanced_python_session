import numpy as np
import math

class Complex:
	"""
	Complex number class
	"""

	def __init__(self, real, imag=0.0):
		"""
		constructor:
			Complex(3, 4)
			Complex(5.0)
		"""
		self.real = real
		self.imag = imag
		self.mag  = np.sqrt(self.real**2 + self.imag**2)
		if self.real == 0.0:
			self.theta = math.pi/2.0
			if self.imag < 0.0:
				self.theta *= -1.0
		else:
			self.theta = np.arctan(self.imag/self.real)
			if self.real < 0.0:
				self.theta -= math.pi			
	

	@classmethod
	def from_polar(cls, mag, theta=0.0, radians=True):
		"""
		Classmethod:
			Complex.from_polar(5, 0.927)
		"""
		_theta = theta
		if not radians:
			_theta = theta * math.pi / 180.0
		_theta =  _theta - (_theta//math.pi) * (math.pi)
		return cls(mag*np.cos(_theta), mag*np.sin(_theta))
		

	def to_polar(self):
		"""
		returns a tuple
		"""
		return (self.mag, self.theta)

	def __str__(self):
		"""
		returns a string format
		"""
		if self.imag < 0.0:
			return '{:.2f} -{:.2f}i'.format(self.real, -self.imag)
		else:
			return '{:.2f} +{:.2f}i'.format(self.real,  self.imag)

	def __eq__(self, other):
		if type(other).__name__ != 'Complex':
			_other =  Complex(other)
		if (self.real == other.real) and (self.imag == other.imag):
			return True
		else:
			return False

	def __add__(self, other):
		"""
		Adds two complex numbers
		"""
		_real = self.real + other.real
		_imag = self.imag + other.imag
		return complex(_real, _imag)

	def __neg__(self):
		return self.__mul__(-1)


	# def __mul__(self, other):
	# 	"""
	# 	multiplies two complex numbers
	# 	"""
	# 	if type(other).__name__ != 'Complex':
	# 		return Complex(other * self.real, other *self.imag)
	# 	else:
	# 		return Complex(self.real * other.real - self.imag * other.imag, 
	# 						self.real * other.imag + self.imag * other.real) 


	def __mul__(self, other):
		"""
		multiplies a complex number with anothernumber real/complex
		"""
		if type(other).__name__ != 'Complex':
			return Complex(other * self.real, other *self.imag)
		else:
			return Complex.from_polar(self.mag * other.mag, 
							theta=self.theta + other.theta)
							 
	def __truediv__(self, other):
		"""
		divides a complex number with anothernumber real/complex
		"""
		if other == 0.0:
			raise ZeroDivisionError
		if type(other).__name__ != 'Complex':
			return Complex(self.real/other, self.imag/other)
		else:
			return Complex.from_polar(self.mag / other.mag, 
							theta=self.theta - other.theta) 

	def __pow__(self, other):
		"""
		exponent of a complex number 
		"""
		if other == 0.0:
			return Complex(1.0, 0.0)
		else:
			return Complex.from_polar(np.pow(self.mag, other), 
							theta=self.theta * other) 

	def __sub__(self, other):
		return self + (-1 * other)

	def mod(self):
		return self.mag

if __name__ == '__main__':
	z1 = Complex(3, 4)
	print(z1)
	print(z1.to_polar())
	print(-z1)
	print((-z1).to_polar())
	z2 = Complex(3, -4)
	print(z1 * z2)
	print(z1/z2)

