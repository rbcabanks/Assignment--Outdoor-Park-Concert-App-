import json
import jsonpickle
from collections import Counter

occurrences=0

def open_json():

    file_name='new_file.json'
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
    newlist=jsonpickle.decode(file_data)

    return newlist
 

def toJson():
    global occurrences

    Dict = {}
    print("""
        Seat Types:
            Front Seat with price $80.  Rows 0 - 4
            Middle Seat with price $50.  Rows 5-10
            Back Seat with price $25.  Rows 11-19")
            -------------------------------------------
            """)

    # user input
    name=input('What is your name?')
    print('CHOOSE A SEAT TYPE: Front, Middle or Back')
    mySeatType = input('Seat Type: ') 
    if not ("Front" in mySeatType or "front" in mySeatType or "back" in mySeatType or "Back" in mySeatType or "middle" in mySeatType or "Middle" in mySeatType):
        print('Invalid response, try again!')
        mySeatType = input('Seat Type: ') 

    myNumberOfTickets = input('NUMBER OF TICKETS : ')   
    myPrice=0
    seatPrice=0
    rows=""


    #evaluating the price and rows based on user inpput
    if(("Front" in mySeatType) or ("front" in mySeatType)):
        seatPrice=80
        rows=rows+("0-4")
    elif(("middle" in mySeatType) or ("Middle" in mySeatType)):
        seatPrice=50
        rows=rows+("5-10")
    elif(("back" in mySeatType) or ("Back" in mySeatType)):
        seatPrice=25
        rows=rows+("11-19")
    
    myPrice=seatPrice*int(myNumberOfTickets)
    num=7.25
    stateTax=myPrice*(float(num)/100)
    myPrice= (myPrice *(1+float(num)/100))
    myPrice=myPrice+5

    #setting values for the dictionary item 
    Dict= {
        "Name":name,
        "SeatType":mySeatType,
        "NumberOfTickets": myNumberOfTickets,
        "Price": myPrice,
        "Rows":rows
    }

    # load the elements into the json file
    lst=[]
    #file_name = 'new_file.json'

    #if there is already an entry
    if(occurrences!=0):
        for elems in open_json():
            lst.append(elems)
    lst.append(Dict)

    #dump the list into the json file 
    with open('new_file.json', 'w') as f:
        json.dump(lst, f, 
            indent=4,  
            separators=(',',': '))

    occurrences=occurrences+1

    # printing the reciept
    print('--------Reciept--------')
    print('Thank you for your order' + name)
    print('Seat Type: '+mySeatType)
    print('Number of Tickets: '+myNumberOfTickets)
    print('x Price Per Ticket: $' +str(seatPrice))
    print('+ State tax of 7.25%: $' +str(stateTax))
    print('+ Added additional mandatory mask fee of $5.00')
    print('-------Total Price-------')
    print('$'+str(myPrice))

"""
    lst=[]
    # Serializing json 
    #json_object = json.dumps(lst, indent = 4)    
        # create a document
    
    filename = 'new_file.json'
    

    else:
        print("Here")
        write_json(Dict)


    lst.append(Dict)
    with open(filename, 'w') as f:
        json.dump(lst, f, 
            indent=4,  
            separators=(',',': '))
        #json.dumps(lst)

    #print("list: ")
    #lst.append(Dict)
    #print(lst)


    # read the whole json file into a variable
    # Writing to sample.json

    with open('new_file.json', "w") as json_file:
        json.dump(lst, json_file, 
            indent=4,  
            separators=(',',': '))
    

 """