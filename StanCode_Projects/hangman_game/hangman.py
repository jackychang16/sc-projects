"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    In this program, user should to set the number of wrong times in guessing.
    When user guesses the character correctly, the program announce the right character
    in which place. Vice versa, user guesses the character wrong, the program cut one chance.
    In each round, the program will remind the user how many chances are left to get wrong and remind
    un-dashed words. Finally, the program publish the answer.
    """
    secret = random_word()
    # we should define the random word as ,the same word,secret.
    ans = (len(secret)*'-')
    n = int(N_TURNS)
    # the number of N_TURNS can not be changed so we need to create another variable
    dash_ans = ans
    print('The world looks like: ', end='')
    print(ans)
    print('You have ' + str(int(n)) + ' guesses left.')
    # your_guess = input('Your guess:')
    # your_guess = your_guess.upper()
    while True:
            your_guess = input('Your guess:')
            your_guess = your_guess.upper()
            string = ''
            for k in range(len(secret)):
                if your_guess == secret[k]:
                    string = string + secret[k]
                else:
                    string = string + dash_ans[k]
                    """User has guessed some correct character, so the program need to take dash or 
                    letter in the last dash_ans
                    """
            dash_ans = string
            if your_guess not in secret:
                n-=1
                print('There is no '+your_guess+"'s in the word." )
            else:
                print('You are correct!')

            if n == 0:
                print('You are completely hung : ( ')
                print('The word was: ' + secret)
                break

            if dash_ans.isalpha():
                print('You win!!')
                print('The word was: '+dash_ans)
                break

            print('The world looks like: ', end='')
            print(dash_ans)
            print('You have ' + str(int(n)) + ' guesses left.')






            # if dash_ans.isalpha():
            #     print('You win!!')
            #     print('The word was: '+dash_ans)
            #     break


            # for i in range(len(secret)):
            #     if ans[i].isalpha():
            #         ans = ans[i]
            #     elif your_guess == secret[i]:
            #         ans = ans + secret[i]
            #
            #     else:
            #         ans = ans + '-'
            #
            #     print(ans)


#
# def judge():
#     your_guess = input('Your guess:')
#     your_guess = your_guess.upper()
#     while True:
#         for j in range(len(random_word())):
#             if your_guess == random_word(j):
#                 print('Your are correct!')
#                 break
#         N_TURNS = N_TURNS - 1
#         break


# def main():
#     """
#
#     """
#
#     ans = (len(random_word())*'-')
#
#     while True:
#         if N_TURNS >0:
#
#             print('The world looks like: ',end='')
#             print(ans)
#             print('You have'+str(N_TURNS)+'guesses left.')
#             your_guess = input('Your guess:')
#             your_guess = your_guess.upper()
#             # judge()
#
#             # for j in range(len(random_word())):
#             #     if your_guess == random_word(j):
#             #         correct = 'Your are correct!'
#
#            # for j in range(len(random_word())):
#            #      if your_guess != random_word(j):
#            #
#            #      print('Your are correct!')
#             while True:
#                 if your_guess != random_word():
#                     N_TURNS = N_TURNS-1
#                     break
#                 else:
#                     print('Your are correct!')
#                     break
#
#
#
#
#
#
#
#
#             for i in range(len(random_word())):
#                 if ans(i).isupper():
#                     ans = ans(i)
#                 elif your_guess == random_word(i):
#                     ans = ans+random_word(i)
#
#                 else:
#                     ans = ans+'-'
#
#                 print(ans)
#
#
#
#
#         else:
#             print('Your are completely hung : ( ')
#             print('The word was: '+random_word())
#             break



def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
