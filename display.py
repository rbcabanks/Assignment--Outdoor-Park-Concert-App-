
import json
import jsonpickle
import buy as buy

#-----------------------------------------------------------------------------
def printAll():

    print("""
            Display
                All the purchases made and the total amount of income/money that the venue has made.
            -------------------------------------------
            """)

    lst=[]
    
    for elems in buy.open_json():
            lst.append(elems)
    
    counter=0
    totalrev=0
    for record in lst:
        print(" ")
        print("------ Guest: "+str(counter+1)+" ------")
        print("Name: "+str(record['Name']))
        print("Email: "+str(record['Email']))
        print("Seat Type: "+str(record['SeatType']))
        print("Number of Tickets: #" + str(record['NumberOfTickets']))
        print("Total Price: $" + str(record['Price']))
        #print("Rows: #"+str(record['Rows']))
        print(" ")
        counter=counter+1
        totalrev=totalrev+record['Price']

    print("-----------------")
    print("Total Revenue: ")
    print("$"+str(totalrev))

