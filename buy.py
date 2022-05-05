import json
import jsonpickle
from collections import Counter

# created global variable so accessible in other pages if needed

# occurrences = 0
# -----------------------------------------------------------------------------


def open_json():

    file_name = 'guest_list.json'
    try:
        newfile = open(file_name, "r")
    except IOError:
        print("Error: File " + file_name + " does not appear to exist.")
        return -1

    # read the file
    file_data = newfile.read()
    # close the file
    newfile.close()
    # decode json into an object
    newlist = jsonpickle.decode(file_data)

    return newlist

# -----------------------------------------------------------------------------


def to_json():
    #global occurrences

    guest_dictionary = {}
    print("""
        Seat Types:
            Front Seat with price $80.  Rows 0 - 4
            Middle Seat with price $50.  Rows 5-10
            Back Seat with price $25.  Rows 11-19")
            -------------------------------------------
            """)

    # user input
    # name
    name = input('What is your name?')
    # email
    email = input('What is your email address?')
    if not("@" in email):
        print("Invalid response, try again!")
        email = input('What is your email address?')
    # seat type
    print('CHOOSE A SEAT TYPE: Front, Middle or Back')
    my_seat_type = input('Seat Type: ')
    # checking that seat type entry is front, middle, or back
    if not ("Front" in my_seat_type or "front" in my_seat_type or "back" in my_seat_type or "Back" in my_seat_type or "middle" in my_seat_type or "Middle" in my_seat_type):
        print('Invalid response, try again!')
        my_seat_type = input('Seat Type: ')

    Rows = 0
    my_number_of_tickets = input('NUMBER OF TICKETS : ')
    my_price = 0
    seat_price = 0
    rows = ""

    # evaluating the price and rows based on user input
    if(("Front" in my_seat_type) or ("front" in my_seat_type)):
        seat_price = 80
        Rows = 1
    elif(("middle" in my_seat_type) or ("Middle" in my_seat_type)):
        seat_price = 50
        Rows = 2
    elif(("back" in my_seat_type) or ("Back" in my_seat_type)):
        seat_price = 25
        Rows = 3

    # evaluating price given state tax and mask
    my_price = seat_price*int(my_number_of_tickets)
    tax_num = 7.25
    state_tax = my_price*(float(tax_num)/100)
    my_price = (my_price * (1+float(tax_num)/100))
    # mask for $5
    my_price = my_price+5

    # setting values for the dictionary item
    guest_dictionary = {
        "Name": name,
        "Email": email,
        "SeatType": my_seat_type,
        "NumberOfTickets": my_number_of_tickets,
        "Price": my_price,
        "Rows": Rows
    }

    # load the elements into the json file
    new_guest_list = []
    #file_name = 'new_file.json'

    # if you want the page to refresh each time...
    # if(occurrences!=0):
    for elems in open_json():
        new_guest_list.append(elems)
    new_guest_list.append(guest_dictionary)

    # dump the list into the json file
    with open('guest_list.json', 'w') as f:
        json.dump(new_guest_list, f,
                  indent=4,
                  separators=(',', ': '))

    #occurrences = occurrences+1

    # printing the reciept
    print('--------Reciept--------')
    print('Thank you for your order' + name)
    print('Email provided' + email)
    print('Seat Type: '+my_seat_type)
    print('Number of Tickets: '+my_number_of_tickets)
    print('x Price Per Ticket: $' + str(seat_price))
    print('+ State tax of 7.25%: $' + str(state_tax))
    print('+ Added additional mandatory mask fee of $5.00')
    print('-------Total Price-------')
    print('$'+str(my_price))
