"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def main():
    """
    User should put the number that define how many steps should the ALPHABET
    move forward in sequence and then give the cipher string.
    Program will decipher world and make you know.

    """

    n = int(input('Secret number: '))
    new_alphabet = build_new_alphabet(n)
    # print(new_alphabet)
    old_world = input('What\'s the ciphered string?')
    old_world = old_world.upper()
    new_world = deciphered(old_world, new_alphabet)
    print('The decipher string is: ' + new_world)




    # print(new_alphabet)


def build_new_alphabet(n):
    new_alphabet = ''
    for i in range(26):
        '''
        The ALPHABET has 26 letters.
        The program should create from the last letter 
        to the first letter in the new ALPHABET. 
        '''
        new = ALPHABET[(i - n +26) % 26]
        new_alphabet = new_alphabet + new
    return new_alphabet


def deciphered(old_world, new_alphabet):
    new_world = ''
    for j in range(len(old_world)):
        if old_world[j].isalpha():
            """
            Every number of ciphered letter, from the first to the last, should be contrasted to 
            the new ALPHABET and decipher to the new world.
            
            """
            num = new_alphabet.find(old_world[j])
            # print(num)
            new_world = new_world + ALPHABET[num]

        else:
            new_world = new_world + old_world[j]

    return new_world


        # print(ALPHABET[num],end='')


    # new_world = decomposed(old_world)
    # print('The deciphered string is:'+str(new_world))



# def deciphered(old_world, new_alphabet):
#     for j in range(len(old_world)):
#         num = old_world.find(new_alphabet)
#         print(num)
#         return num


    # def deciphered(old_world,new_alphabet):
    #     for j in range(len(old_world)):
    #         num = old_world.find(new_alphabet)
    #         print(num)
    #         return num
    #

#
# def decomposed(old_world):
#     # for i in range(26):
#     #     new = ALPHABET[(i + n) % 26]
#     #     new_alphabet = new_alphabet + new
#     # print(new_alphabet)
#     # for j in range(len(old_world)):
#     #     num = old_world.find(new_alphabet)
#     #     print(num)
#         return num
#
#     pass


        # print('The complement of ' + str(new_dna) + ' is ', end='')
        #

        # , ALPHABET, new_world,

    # old_world =






#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

