
import json
import jsonpickle
import buy as buy

#-----------------------------------------------------------------------------
def printAll():
    lst=[]
    if(buy.occurrences!=0):
        for elems in buy.open_json():
            lst.append(elems)
    else:
        print("No Guests Yet")
    
    counter=0
    for record in lst:
        print(" ")
        print("------ Guest: "+str(counter+1)+" ------")
        print("Name: "+str(record['Name']))
        print("Seat Type: "+str(record['SeatType']))
        print("Number of Tickets: #" + str(record['NumberOfTickets']))
        print("Total Price: $" + str(record['Price']))
        #print("Rows: #"+str(record['Rows']))
        print(" ")
        counter=counter+1

