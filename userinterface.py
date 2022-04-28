import io

import outdoorParkConcertExample as outdoorParkConcertExample
import buy as buy
import display as display
import search as search

dist,x,y,dx,dy=-1,-1,-1,-1,-1

"""
    Student: Rebecca Banks
    Module: gladysUserInterface
    Description: This module provides the user with an easy UX that asks for an input value that directs them to different functions.
"""
# the user interface section
def header():
    print(' ')
    print(' ')
    print("---------------------------------------")
    print("       Outdoor Park Concert App        ")
    print("---------------------------------------")
    print("[V]iew/display available seating")
    print("[B]uy/purchase a ticket and provide receipt with  state tax of 7.25% including an additional mandatory mask fee of $5.00")
    print("[S]earch by name will display the tickets purchased by a user with a specific name.")
    print("[D]isplay all purchases.")
    print("[Q]uit")
    print("---------------------------------------")


# the code that interprets the user input
def runApp():
    guest_list=[]
    guest_list=buy.open_json

    header()
    userQuit = False
    while (not userQuit):

        # menu
        header()

        # get first character of input
        userInput = input("Enter a command:")
        lowerInput = userInput.lower()
        firstChar = lowerInput[0:1]

        # quit
        if firstChar == 'q':
            print('=====QUIT=====')
            userQuit = True

        elif firstChar == 'v':
            print('[V]iew/display available seating')
            outdoorParkConcertExample.print_matrix()

        elif firstChar == 'b':
            print('[B]uy/purchase a ticket and provide receipt with  state tax of 7.25% including an additional mandatory mask fee of $5.00')
            buy.toJson()

        elif firstChar == 's':
            print('[S]earch by name will display the tickets purchased by a user with a specific name.')
            search.search()

        elif firstChar == 'd':
            print('[D]isplay all purchases.  Prints all the purchases made and shows the total amount of income/money that the venue has made.')
            display.printAll()
        else:
            print("ERROR: " + firstChar + " is not a valid command")

    print("\n")
    print("Thank you for using the Outdoor Park Concert App!")
    print("\n")

runApp()