import io

import outdoorParkConcertExample as outdoorParkConcertExample
import buy as buy

dist,x,y,dx,dy=-1,-1,-1,-1,-1

"""
    Student: Rebecca Banks
    Module: gladysUserInterface
    Description: This module provides the user with an easy UX that asks for an input value that directs them to different functions.
"""

def header():
    print(' ')
    print(' ')
    print("--------------------------------------------")
    print("---- WELCOME TO THE GLADYS WEST MAP APP ----")
    print("--------------------------------------------")
    
    options=['Type c to set current position','Type d to set destination position','Type m to map – which tells the distance','Type t to run module tests','Type q to quit']
    for item in options:
        print(' - '+item)
    print("_____________________________________________")
    print(' ')

def runApp():
    header()
    userQuit = False
    while (not userQuit):

        # menu
        header()

        # get first character of input
        userInput = input("Enter a command:")
        lowerInput = userInput.lower()
        firstChar = lowerInput[0:1]

        # menu choices, use a switch-like if-elif control structure

        # quit
        if firstChar == 'q':
            print('=====QUIT=====')
            userQuit = True

        # run some tests (this is part 1 of 2)
        elif firstChar == 'v':
            print('[V]iew/display available seating')
            outdoorParkConcertExample.print_matrix()

        elif firstChar == 'b':
            print('[B]uy/purchase a ticket and provide receipt with  state tax of 7.25% including an additional mandatory mask fee of $5.00')
            buy.toJson()
        elif firstChar == 'd':
            print('[D]isplay all purchases.  Prints all the purchases made and shows the total amount of income/money that the venue has made.')

        else:
            print("ERROR: " + firstChar + " is not a valid command")

    print("\n")
    print("Thank you for using the Gladys West Map App!")
    print("\n")

runApp()