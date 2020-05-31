from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
	a = Fraction(1, 2)
	b = Fraction(3, 4)
	c = Fraction(10, 6)
	num, den = product([a, b, c])
	d = Fraction(num, den)
	print(d)

