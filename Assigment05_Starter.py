# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# Tony Le, 11-04-19, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python Dictionary.
open(objFile, "a")
objFile = open(objFile, "r")
for row in objFile:
    strData = row.split(",") # Returns a list!
    dicRow = {"task": strData[0], "priority": strData[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        if not lstTable:
            print("No data in list")
        else:
            for row in lstTable:
                print(row['task'] + ", " + row['priority'])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = str(input("Enter a task: "))
        strPriority = str(input("Enter a priority value: "))
        dicRow = {"task": strTask, "priority": strPriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        strDel = input("Do you wish to delete the latest entry? Enter 'y' or 'n': ")
        if strDel.lower() == "y":
            del lstTable[len(lstTable)-1]
            print("Latest entry deletion successful")
        else:
            print("No entries have been removed")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        for d in lstTable:
            objFile.write(d['task'] + ", " + d['priority'] + '\n')
        objFile.close()
        print("Data was saved!")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Menu closed")
        break  # and Exit the program
