"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Let user put the DNA strand first.
    The program will make all the letter into upper worlds.
    And then find the complement strand of user's DNA strand.
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    # new_dna = build_complement(dna)
    # print(str(new_dna))
    print(build_complement(dna))
    print('The complement of ' + str(dna) + ' is ' + build_complement(dna) , end='')


def build_complement(dna):
    new_dna=''
    for ch in dna:
        if ch =='A':
            new_dna +='T'
        elif ch == 'T':
            new_dna += 'A'
        elif ch == 'G':
            new_dna +='C'
        elif ch == 'C':
            new_dna +='G'
    return new_dna



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
