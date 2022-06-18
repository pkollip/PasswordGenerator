import random
import string

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
    print("Welcome to the password generator!\n")
    length = input("What would you like the length of the password to be?\n")
    symbols = input("Would you like the password to include symbols? (Y/N)\n")
    numbers = input("Would you like the password to include numbers? (Y/N)\n")
    lowercase = input("Would you like the password to include lowercase letters? (Y/N)\n")
    uppercase = input("Would you like the password to include uppercase letters? (Y/N)\n")
    similar = input("Should the password exclude similar characters? (Y/N)\n")
    returned = [length, symbols, numbers, lowercase, uppercase, similar]
    for i in range(1, len(returned)):
        if returned[i] == "Y" or returned[i] == "y":
            returned[i] = True
        else:
            returned[i] = False
    return returned

def main():
    [length, symbols, numbers, lowercase, uppercase, similar] = intro()
    password = []

    if (lowercase and uppercase and symbols and numbers):
        if (similar):
            password = random.sample(string.digits + string.ascii_letters + string.punctuation, int(length))
        else:
            for x in range(int(length)):
                password.append(random.choice(string.digits + string.ascii_letters + string.punctuation))
    elif (not symbols and numbers):
        if (lowercase and uppercase):
            for x in range(int(length)):
                password.append(random.choice(string.digits + string.ascii_letters))
        elif (not lowercase and uppercase):
            for x in range(int(length)):
                password.append(random.choice(string.digits + string.ascii_uppercase))
        elif (lowercase and not uppercase):
            for x in range(int(length)):
                password.append(random.choice(string.digits + string.ascii_lowercase))
    elif (not numbers and symbols):
        if (lowercase and uppercase):
            for x in range(int(length)):
                password.append(random.choice(string.digits + string.ascii_letters))
        elif (not lowercase and uppercase):
            for x in range(int(length)):
                password.append(random.choice(string.digits + string.ascii_uppercase))
        elif (lowercase and not uppercase):
            for x in range(int(length)):
                password.append(random.choice(string.digits + string.ascii_lowercase))
    print("".join(password))
    #if (lowercase and uppercase):
     #   password.append(random.choice(string.ascii_letters) for x in range())

if __name__ == "__main__":
    main()