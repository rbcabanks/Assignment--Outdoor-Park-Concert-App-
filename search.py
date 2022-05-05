
import json
import jsonpickle
import buy as buy

# -----------------------------------------------------------------------------


def search():
    print("""

        Enter a name to search to display the tickets purchased by that user.
            -------------------------------------------
            """)

    # user input
    name = input('Enter name to search: ')
    guest_list = []
    in_here = False

    # appending all elements in the json to the list
    for elems in buy.open_json():
        guest_list.append(elems)

    # looping through all elements to find the elements with that specific name
    #   if found, prints all of that element's data
    for elems in guest_list:
        if (name in elems['Name']):
            print("---------------------------")
            print("Name: "+str(elems['Name']))
            print("Email: "+str(elems['Email']))
            print("Seat Type: "+str(elems['SeatType']))
            print("Number of Tickets: #" + str(elems['NumberOfTickets']))
            print("Total Price: $" + str(elems['Price']))
            print("Rows: #"+str(elems['Rows']))
            print(" ")
            in_here = True
        else:
            continue

    # if name is not found
    if (in_here == False):
        print("That name is not present in our database")
