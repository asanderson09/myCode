#!/usr/bin/env python3

devPoints = 0
counter = 0
questions = 5

print("\nWelcome to the Dev test! All Questions are yes/no or true/false")
print("\nPlease answer honestly and good luck")

while (questions > 0):
    print('\nQuestion 1: Have you ever cried while writing code: ')
    answer = input('Please enter Y or N :')

    if answer.casefold() == 't' or answer.casefold() =='y':
        devPoints += 1

    questions -= 1
    

    print('\nHave you ever thought of possible alternative careers when your code wasn\'t working? ')
    answer = input('Please enter y or n :')

    if answer.casefold() == 't' or answer.casefold() =='y':
        devPoints += 1
    
    questions -= 1

    print('\nYou have yelled cheered or expressed outward emotion during a coding session? ')
    answer = input('Please enter y or n :')

    if answer.casefold() == 't' or answer.casefold() =='y':
        devPoints += 1
    
    questions -= 1

    print('\nYou feel like you are going to get exposed for what you don\'t know?')
    answer = input('Please enter T or F :')

    if answer.casefold() == 't' or answer.casefold() =='y':
        devPoints += 1

    questions -= 1

    print('\nYou copy and paste code?')
    answer = input('Please enter T or F :')

    if answer.casefold() == 't' or answer.casefold() =='y':
        devPoints += 1

    questions -= 1


print("The results are in!!!!!")

if devPoints >= 4:
    print("Congrats you are an amazing dev")
    break
elif devPoints >=2 and<=3:
    print("It's ok to be mediocre")
    break
else print("Choose another profession.. This aint it!)
