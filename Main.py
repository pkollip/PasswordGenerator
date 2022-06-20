import random
import string
import math

"""
Author: Praval Kollipara

Description:
    This program takes in user inputted values to produces a randomly generate password. 

Contributors:
    NONE

My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
def intro():
    length = 0
    symbols = math.inf
    numbers = math.inf

    print("Welcome to the password generator!\n")
    length = int(input("What would you like the length of the password to be?\n"))
    while (symbols >= length):
        symbols = int(input("How many symbols would you like?\n"))
    while (numbers >= (length - symbols)):
        numbers = int(input("How many numbers would you like?\n"))
    lowercase = input("Would you like the password to include lowercase letters? (Y/N)\n")
    uppercase = input("Would you like the password to include uppercase letters? (Y/N)\n")
    returned = [length, symbols, numbers, lowercase, uppercase]
    for i in range(3, len(returned)):
        if returned[i] == "Y" or returned[i] == "y":
            returned[i] = True
        else:
            returned[i] = False
    return returned

def main():
    [length, symbols, numbers, lowercase, uppercase] = intro()
    password = []

    for i in random.sample(string.punctuation, int(symbols)):
        password.append(i)
    for i in random.sample(string.digits, int(numbers)):
        password.append(i)


   # if (uppercase and lowercase):


if __name__ == "__main__":
    main()