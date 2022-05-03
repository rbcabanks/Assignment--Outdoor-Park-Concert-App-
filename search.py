
import json
import jsonpickle
import buy as buy

#-----------------------------------------------------------------------------
def search():
    print("""

        Enter a name to search to display the tickets purchased by that user.
            -------------------------------------------
            """)

    # user input
    name=input('Enter name to search: ')
    lst=[]
    inHere=False
    for elems in buy.open_json():
        lst.append(elems)
    
    for elems in lst:
        if (name in elems['Name']):
            print("---------------------------")
            print("Name: "+str(elems['Name']))
            print("Email: "+str(elems['Email']))
            print("Seat Type: "+str(elems['SeatType']))
            print("Number of Tickets: #" + str(elems['NumberOfTickets']))
            print("Total Price: $" + str(elems['Price']))
            print("Rows: #"+str(elems['Rows']))
            print(" ")
            inHere=True
        else:
            continue

    if (inHere==False):
        print("That name is not present in our database")