
import json
import jsonpickle
import buy as buy

# -----------------------------------------------------------------------------


def print_all():

    print("""
            Display
                All the purchases made and the total amount of income/money that the venue has made.
            -------------------------------------------
            """)

    guest_list = []

    for elems in buy.open_json():
        guest_list.append(elems)

    counter = 0
    total_revenue = 0
    for record in guest_list:
        print("\t")
        print("------ Guest: "+str(counter+1)+" ------")
        print("Name: "+str(record['Name']))
        print("Email: "+str(record['Email']))
        print("Seat Type: "+str(record['SeatType']))
        print("Number of Tickets: #" + str(record['NumberOfTickets']))
        print("Total Price: $" + str(record['Price']))
        print("\t")
        counter = counter+1
        total_revenue = total_revenue+record['Price']

    print("-----------------")
    print("Total Revenue: ")
    print("$"+str(total_revenue))
