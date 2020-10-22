"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program helps user to contrast the short DNA strand
    in each part of the long DNA strand.
    As the matter, the program should compute how many units
    in the short and long DNA strand and then know how many times
    to contrast.


    """

    long_sequence = input('Please give me a DNA sequence to search: ')
    long_sequence = long_sequence.upper()
    short_sequence =input('What DNA sequence would you like to match?')
    short_sequence = short_sequence.upper()

    final_strand = compare(short_sequence,long_sequence)
    print('The best match is ' + str(final_strand))



def compare(short_sequence,long_sequence):
    a = len(long_sequence)
    b = len(short_sequence)
    """
    a-b+1 = How many times to contrast. 
    """
    max = 0
    # max is the biggest number of ans recently.
    for i in range(a-b+1):

        ans = 0
        # ans= short DNA strand has how many same alphabet in the fragment of  long DNA strand.
        for j in range(b):
            """
            In the short DNA strand, every alphabet should be comparison.
            """
            if short_sequence[j] == long_sequence[i+j]:
                ans+=1
        if ans>max:
            max = ans
            final_strand = long_sequence[i:b+i]
    return final_strand



# def main():
#     S = 'ATTCCATGG'
#     A = 'TAG'
#     MAX = 0
#
#     for i in range(len(S)-len(A)+1):
#         ans = 0
#         for j in range(len(A)):
#             if A[j] == S[j+i]:
#                 ans+=1
#         if ans > MAX:
#             MAX = ans
#             final = (S[i:len(A)+i])
#     print(final)


















###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
