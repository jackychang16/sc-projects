"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 5




def main():
	'''

	This program produce part of the rocket body separately
	and finish the whole work at the end.

	'''
	head()
	belt()
	upper()
	lower()
	belt()
	head()



def head():
	'''
	The figure of the first loop has been defined by the SIZE.
	Under the first loop, the number of second loop was depending on
	how many symbols in each line.
	'''
	for i in range(SIZE):
		for j in range(SIZE,i,-1):
			print(" ",end='')
		for k in range(i+1):
			print('/',end='')
		for l in range(i + 1):
			print('\\',end='')
		print('')

def belt():

	print('+',end='')
	for i in range(SIZE*2):
		print('=',end='')
	print('+')

def upper():
	for i in range(SIZE):
		print('|',end='')
		for j in range(SIZE-1,i,-1):
			print('.',end='')
		for j in range(i+1):
			print('/',end='')
			print('\\', end='')
		for j in range(SIZE-1,i,-1):
			print('.',end='')
		print('|')


def lower():
	for i in range(SIZE):
		print('|',end='')
		for l in range(i):
			print('.',end='')
		for k in range(SIZE,i,-1):
			print('\\/',end='')
		for l in range(i):
			print('.', end='')
		print('|')







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()