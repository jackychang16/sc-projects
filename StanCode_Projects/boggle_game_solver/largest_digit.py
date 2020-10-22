"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9

#
# def find_largest_digit(n):
# 	"""
# 	input: an integer
# 	return: a biggest digit in this integer
# 	"""
# 	# no matter positive or negative integer
# 	if n < 0:
# 		n = -n
# 	# the digit which stay to the final
# 	if n < 10:
# 		return n
# 	# if 10 <= integer <100 which means only two digits needed to compare
# 	if n < 100:
# 		# units digit
# 		c = n % 10
# 		# tens digit
# 		d = n // 10
# 		if c >= d:
# 			return c
# 		else:
# 			return d
#
# 	b = n % 100 // 10
# 	a = n % 10
# 	# this condition compared unit digit with tens digit and stay the bigger one
# 	if b >= a:
# 		n = n // 100 * 10 + b
# 	else:
# 		n = n // 100 * 10 + a
# 	# repete this function
# 	return find_largest_digit(n)


def find_largest_digit(n):
	if n <= 0:
		n *= -1

	if n < 10:
		return n
	else:
		digit_1 = n % 10
		digit_2 = find_largest_digit(n//10)
		if digit_1 >= digit_2:
			return digit_1
		else:
			return digit_2


if __name__ == '__main__':
	main()
