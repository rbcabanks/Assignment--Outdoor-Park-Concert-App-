import io
import json
import jsonpickle
import view as view
import buy as buy
import display as display
import search as search

def pretty_json(json_string):
    """
    turns json into pretty printed json
    """

    parsed = json.loads(json_string)
    result = json.dumps(parsed, indent=4, sort_keys=True)

    return result

#-----------------------------------------------------------------------------
def save_file(guest_lst):
    # save a file name cupcake-output.json to disk

    #
    # write a object as json to disk
    #

    # attempt to write a file
    file_name = "new_file.json"
    try:
        guest_file = open(file_name, "w")
    except IOError:
        print("Error: File " + file_name + " does not appear to exist.")
        return -1
    

    # encode object into a json string
    guest_json = jsonpickle.encode(guest_lst)

    # write file
    guest_file.write(pretty_json(guest_json))

    # close file
    guest_file .close()

    print("The %s file has been opened and saved to disk." % (file_name))


#-----------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------
# the code that interprets the user input
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

        # quit
        if firstChar == 'q':
            print('=====QUIT=====')
            userQuit = True

        elif firstChar == 'v':
            print('[V]iew/display available seating')
            view.print_matrix()

        elif firstChar == 'b':
            print('[B]uy/purchase a ticket and provide receipt with  state tax of 7.25% including an additional mandatory mask fee of $5.00')
            buy.toJson()

        elif firstChar == 's':
            print('[S]earch by name will display the tickets purchased by a user with a specific name.')
            search.search()

        elif firstChar == 'd':
            print('[D]isplay all purchases.')
            display.printAll()
        else:
            print("ERROR: " + firstChar + " is not a valid command")

    guest_list=[]
    guest_list=buy.open_json()
    save_file(guest_list)
    print("\n")
    print("Thank you for using the Outdoor Park Concert App!")
    print("\n")

runApp()