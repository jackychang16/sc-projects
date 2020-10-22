"""
File: boggle.py
Name:Jacky
----------------------------------------
This program lets user to input alphabets which arrange on square.
And this program will print words which combined on the neighbor alphabets.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
SIZE = 4
dictionary_list = {}


def main():
	"""
	boggle list let user inputs  all alphabets and gives any alphabet a position.
	"""
	boggle = []
	# if user input a wrong formats, the switch will keep on False and this program will print Illegal input
	switch = False
	for i in range(SIZE):
		if switch is True:
			break
		boggle_line = input(f'{i+1} row of letters:')
		boggle_line= boggle_line.split()
		if len(boggle_line) != SIZE:
			print('Illegal input')
			switch = True
			break
		for alphabet in boggle_line:
			if len(alphabet) != 1:
				print('Illegal input')
				switch = True
				break
		boggle.append(boggle_line)
	# print(boggle)
	# let the world in the FILE = 'dictionary.txt' to the dictionary_list
	read_dictionary()
	# let any alphabet have own position
	map_dict = {}
	# if the neighbor alphabet combined surpass  4 units and this world in the dictionary_list
	correct_word_list = []
	# define any position where can connect
	if switch is False:
		for x in range(SIZE):
			for y in range(SIZE):
				map_dict[(x, y)] = {}
				map_dict[(x, y)]['alphabet'] = boggle[x][y]
				if x==0 and y==0:
					map_dict[(x,y)]['map'] = [(x+1,y),(x,y+1),(x+1,y+1)]
				elif x==0 and y==SIZE-1:
					map_dict[(x,y)]['map'] = [(0,y-1),(1,y-1),(1,y-1)]
				elif x==SIZE-1 and y== 0 :
					map_dict[(x,y)]['map'] = [(x-1,0),(x-1,1),(x,1)]
				elif x==SIZE-1 and y==SIZE-1:
					map_dict[(x,y)]['map'] = [(x-1,y),(x-1,y-1),(x,y-1)]
				elif x==0:
					map_dict[(x,y)]['map'] = [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1)]
				elif x == SIZE-1:
					map_dict[(x,y)]['map'] = [(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1)]
				elif y == 0:
					map_dict[(x,y)]['map'] = [(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y)]
				elif y == SIZE-1:
					map_dict[(x,y)]['map'] = [(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y)]
				else:
					map_dict[(x,y)]['map'] = [(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y)]
		for i in range(SIZE):
			for j in range(SIZE):
				permutation(map_dict,(i,j),correct_word_list)
		print(f'There are {len(correct_word_list)} words in total')


def permutation(map_dict,position,correct_word_list, coordinate_list=[]):
	coordinate_list.append(position)
	maybe_word = (num_to_string(coordinate_list, map_dict))
	# print(num_to_string(coordinate_list, map_dict))
	if len(maybe_word) >=4 and maybe_word in dictionary_list and maybe_word not in correct_word_list:
		correct_word_list.append(maybe_word)
		print(f'Found "{maybe_word}"')
	for next_position in map_dict[position]['map']:
		if next_position not in coordinate_list:
			if has_prefix(maybe_word):
				permutation(map_dict,next_position,correct_word_list, coordinate_list)
	coordinate_list.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	global dictionary_list
	with open(FILE, 'r') as f:
		for line in f:
			words = line.split()
			for word in words:
				dictionary_list[word] = word
	return dictionary_list


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for dict_word in dictionary_list:
		if dict_word.startswith(sub_s):
			return True
	return False


def num_to_string(coordinate_list, map_dict):
    ans = ""
    for figure in coordinate_list:
        ans += map_dict[figure]['alphabet']
    return ans


if __name__ == '__main__':
	main()
