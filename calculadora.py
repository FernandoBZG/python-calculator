

#Operations
def multi(a,b):
	c = a * b
	return c
def divi(a,b):
	c = a / b
	return c
def sum(a,b):
	c = a + b
	return c
def sub(a,b):
	c = a - b
	return c
	#Process
while True:
	print(" Operations: \n 1 - Multication \n 2 - Sum \n 3 - Subtration\n 4 - Division")
	oper = (input("What's The operation? "))

	number1 = input("First Number: ")
	number2 = input("Second Number: ")
	try:
		operation = int(oper)

		number11 = float(number1)
		number22 = float(number2)
	except:
		print('Something went wrong.')
		break
	    
	if operation == 2:
		result = sum(number11, number22)
	elif operation == 1:
		result = multi(number11, number22)
	elif operation == 4:
		result = divi(number11, number22)
	elif operation == 3:
		result = sub(number11, number22)

	print(result, '\n')

	retry = input('Want to do another operation? \n Yes or No: ').lower()
	if retry == 'yes':
		continue
	else:
		print('Bye!')
		break