import json
import jsonpickle
from collections import Counter

occurrences=0
lst=[]
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
    newfile=jsonpickle.decode(file_data)
 

def toJson():
    global occurrences
    global list
    Dict = {}
    #Dict = dict.fromkeys(['SeatType', 'NumberOfTickets', 'Price','Rows'])
    print("""
        Seat Types:
            Front Seat with price $80.  Rows 0 - 4
            Middle Seat with price $50.  Rows 5-10
            Back Seat with price $25.  Rows 11-19")
            -------------------------------------------
            """)
    print('CHOOSE A SEAT TYPE: Front, Middle or Back')
    mySeatType = input('Seat Type: ') 
    if not ("Front" in mySeatType or "front" in mySeatType or "back" in mySeatType or "Back" in mySeatType or "middle" in mySeatType or "Middle" in mySeatType):
        print('Invalid response, try again!')
        mySeatType = input('Seat Type: ') 

    myNumberOfTickets = input('NUMBER OF TICKETS : ')   
    myPrice=0
    seatPrice=0
    rows=""

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

    Dict= {
        "SeatType":mySeatType,
        "NumberOfTickets": myNumberOfTickets,
        "Price": myPrice,
        "Rows":rows
    }

    # load the first element
    lst=[]
    file_name = 'new_file.json'

    lst.append(Dict)

    with open(file_name, 'w') as f:
        json.dump(lst, f, 
            indent=4,  
            separators=(',',': '))

    occurrences=occurrences+1
    """
    Dict['SeatType'] = [mySeatType]
    Dict['NumberOfTickets'] = [myNumberOfTickets]
    Dict['Price'] = [myPrice]
    Dict['Rows'] = [rows]
"""

    print('--------Reciept--------')
    print('Thank you for your order')
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