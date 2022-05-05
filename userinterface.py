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
    file_name = "guest_list.json"
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
    user_quit = False
    while (not user_quit):

        # menu
        header()

        # get first character of input
        user_input = input("Enter a command:")
        lower_input = user_input.lower()
        first_char = lower_input[0:1]

        # quit
        if first_char == 'q':
            print('=====QUIT=====')
            user_quit = True

        elif first_char == 'v':
            print('[V]iew/display available seating')
            view.print_matrix()

        elif first_char == 'b':
            print('[B]uy/purchase a ticket and provide receipt with  state tax of 7.25% including an additional mandatory mask fee of $5.00')
            buy.to_json()

        elif first_char == 's':
            print('[S]earch by name will display the tickets purchased by a user with a specific name.')
            search.search()

        elif first_char == 'd':
            print('[D]isplay all purchases.')
            display.print_all()
        else:
            print("ERROR: " + first_char + " is not a valid command")

    guest_list=[]
    guest_list=buy.open_json()
    save_file(guest_list)
    print("\n")
    print("Thank you for using the Outdoor Park Concert App!")
    print("\n")

runApp()