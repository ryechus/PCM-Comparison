import sys
import re

def main(*args, **kwargs):
	expression = r"\d+"
	expression = re.compile(expression)
	number = args[0]
	if isinstance(args[0], list):
		number = args[0][1]
	if not isinstance(number, int) and not expression.match(number):
		raise TypeError("not a number")
	number = int(number)
	i = 2
	arr = []
	skip = False
	while i <= number:
		if number % i == 0:
			arr.append(i)
			number = number / i
			i = 2
		else:
			i += 1
	if 'object' in kwargs and kwargs['object']:
		return arr
	print arr

if __name__  == '__main__':
	main(sys.argv)
