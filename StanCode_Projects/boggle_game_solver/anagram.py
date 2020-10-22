"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary_list = {}


def main():
    read_dictionary()
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    words = input("Find anagrams for: ")
    finally_total_words = find_anagrams(words)
    print(f'{len(finally_total_words)} anagrams: {finally_total_words}')


def read_dictionary():
    global dictionary_list
    with open(FILE, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                dictionary_list[word] = word
    return dictionary_list


def find_anagrams(s):
    num_list = []
    total_list = []
    for i in range(len(s)):
        num_list.append(i)
    find_anagrams_helper(s, num_list, [], [], total_list)
    return total_list


def find_anagrams_helper(s, num_list, current_word_list, current_num, total_list):
    if len(current_num) == len(s):
        maybe_word = num_to_string(current_num, s)
        if maybe_word not in total_list and maybe_word in dictionary_list:
            total_list.append(maybe_word)
            print("Searching...")
            print(f'Found: {maybe_word}')
    else:
        for num in num_list:
            if num not in current_num:
                # choose
                current_num.append(num)
                # explore
                maybe_letter = num_to_string(current_num,s)
                if len(maybe_letter) == 1:
                    find_anagrams_helper(s, num_list, current_word_list, current_num, total_list)
                else:
                    if has_prefix(maybe_letter):
                        find_anagrams_helper(s, num_list, current_word_list, current_num, total_list)
                # un-choose
                current_num.pop()


# let numbers transfer to words
def num_to_string(nums,words):
    ans = ""
    for num in nums:
        ans += words[num]
    return ans

# if connected alphabets which not in the dictionary, this program will not check this alphates string with
# connected alphabet
def has_prefix(sub_s):
    for dict_word in dictionary_list:
        if dict_word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
