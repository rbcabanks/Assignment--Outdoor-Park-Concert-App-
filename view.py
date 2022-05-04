import json
import jsonpickle
import buy as buy



"""
This code creates a 2d list (2d matrix) that can store seating.
The matrix is populated with a since all seats are available
"""

#-----------------------------------------------------------------------------
def loop(n_row,n_col,range1,range2,val,numlst,seating):
    # available + taken seat
    available_seat = 'a'
    taken_seat='X'
    # Front
    for r in range(range1,range2):
        #formatting (counter)
        print(val,r, end="\t")
        row1=[]

        #checks to make sure there is a row in between by only looking for even number rows and row 0 
        if (r == 0 or (r % 2==0)):
            #looping through and creating the matrix for the front 4 rows
            for c in range(n_col):
                if (c==0):
                    if (len(numlst)!=0):
                        for x in range (0,numlst[0]):
                            row1.append(taken_seat)
                            c=c+1
                        row1.append(available_seat)
                        row1.append(available_seat)
                        c=c+2
                        #popping the top value of the list after it has been printed
                        numlst.pop(0)
                    else:
                        #works if there is no more values to add in numList 
                        row1.append(available_seat)

                #fills in the rest of row1 after the first initial append
                elif(len(row1)<n_col):
                    # for the case that a group is too large for one row. The code will continue adding members of the group in the next row
                    if (len(numlst)!=0):
                        if((n_col-len(row1))<numlst[0]+2):
                            num=numlst[0]-(n_col-len(row1))

                            for x in range(0,n_col-len(row1)):
                                row1.append(taken_seat)
                                c=c+1
                            numlst.pop(0)
                            numlst.insert(0,num)
                            break
                        
                        for x in range (0,numlst[0]):
                            row1.append(taken_seat)
                            c=c+1

                        row1.append(available_seat)
                        row1.append(available_seat)
                        c=c+2    
                        numlst.pop(0)
                    else:
                        row1.append(available_seat)
                elif((len(numlst)!=0)and len(row1)>=n_col):
                    print("Not enough space")
                    break
        else:
            for c in range(n_col):
                row1.append(available_seat)

        seating.append(row1)
        for c in range(n_col):
            print(seating[r][c],end=" ")
        print()

#-----------------------------------------------------------------------------
def print_matrix():
    print("""
        Seating Chart Keys:
            [a] - available seat
            [X] - taken seat
             F - Front Rows 0-4
             M - Middle Rows 5-10
             B - Back Rows 11-19
            -------------------------------------------
            """)
    print("        a b c d e f g h i j k l m n o p q r s t u v w x y z")
    print("")
    
    
    frontLst=[]
    midLst=[]
    backLst=[]

    #if want a new session for every run... add 
    # if(buy.occurrences!=0):

    for elems in buy.open_json():
        if (elems["Rows"]==1):
            #print('Front')
            frontLst.append(elems)
        elif (elems["Rows"]==2):
            #print('Middle')
            midLst.append(elems)
        elif (elems["Rows"]==3):
            #print('Back')
            backLst.append(elems)

    # our test matrix has 4 rows and 10 columns
    n_row = 20
    n_col = 26


    # create some available seating
    seating = []

    #creating variables for the ranges
    third1=int(n_row/3)-1
    third2=int(2*(n_row/3))-1

    counter=0

    # Front
    numlst=[]
    for elems in frontLst:
        numlst.append(int(elems["NumberOfTickets"]))

    loop(n_row,n_col,0,third1,"F",numlst,seating)

    # Middle
    numlst2=[]
    for elems in midLst:
        numlst2.append(int(elems["NumberOfTickets"]))

    loop(n_row,n_col,third1,third2-1,"M",numlst2,seating)

    # Back
    numlst3=[]
    for elems in backLst:
        numlst3.append(int(elems["NumberOfTickets"]))

    loop(n_row,n_col,third2-1,n_row,"B",numlst3,seating)

