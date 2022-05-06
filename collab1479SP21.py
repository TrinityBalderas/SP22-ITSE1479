# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2022";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Alvarez - call to function goes here
    jumpTable['3'] = stub                 # Appiah - call to function goes here
    jumpTable['4'] = balderasRPS          # Balderas - call to function goes here
    jumpTable['5'] = stub                 # Butler - call to function goes here
    jumpTable['6'] = stub                 # Kennedy - call to function goes here
    jumpTable['7'] = stub                 # Long - call to function goes here
    jumpTable['8'] = stub                 # Nguyen - call to function goes here
    jumpTable['9'] = stub                 # Overby - call to function goes here
    jumpTable['10'] = stub                # Robarge - call to function goes here
    jumpTable['11'] = stub                # Roeper - call to function goes here
    jumpTable['12'] = stub                # Subba - call to function goes here
    jumpTable['13'] = stub                # Thorne - call to function goes here
    jumpTable['14'] = stub                # Thurman - call to function goes here
    jumpTable['15'] = stub                # Valdez - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Alvarez")
    print("3.  Appiah")
    print("4.  Balderas")
    print("5.  Butler")
    print("6.  Kennedy")
    print("7.  Long")
    print("8.  Nguyen")
    print("9.  Overby")
    print("10. Robarge")
    print("11. Roeper")
    print("12. Subba")
    print("13. Thorne")
    print("14. Thurman")
    print("15. Valdez")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.  
#  
# FunctionName:  lastnameFunction(your parameters)
# *****************************************************************************************

# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def stub():
    print()
    print()

    print("Not implemented at this time.  Check back later.")
    print("Press ENTER to continue.")
    input()    

# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()

import random
def balderasRPS():
    done = False
    while not done:
        print(
    """**************************************
    * Rock Paper Scissors *
    **************************************
    (1) Rock
    (2) Paper
    (3) Scissors

    (x) Exit""")
        user = input("pick an option ")
        comput = random.randint(1, 3)
        #Tie
        if (comput == 1 and user == '1'):
            print("You picked Rock \nThe computer picked Rock \nYou Tied")
        elif(comput == 2 and user == '2'):
            print("You picked Paper \nThe computer picked Paper \nYou Tie")
        elif(comput == 3 and user == '3'):
            print("You picked Scissors \nThe computer picked Scissors \nYou Tie")

        #Computer Rock
        elif (comput == 1 and user == '2'):
            print("The computer picked Rock \nYou picked Paper \nYou Win")
        elif (comput == 1 and user == '3'):
            print("The computer picked Rock \nYou picked Scissors \nYou Lose")

        #Computer Paper
        elif (comput == 2 and user == '1'):
            print("The computer picked Paper \nYou picked Rock \nYou Lose")
        elif (comput == 2 and user == '3'):
            print("The computer picked Paper \nYou picked Scissors \nYou Win")

        #Computer Scissors
        elif (comput == 3 and user == '1'):
            print("The computer picked Scissors \nYou picked Rock \nYou Win")
        elif (comput == 3 and user == '2'):
            print("The computer picked Scissors \nYou picked Paper \nYou Lose")

        #User Rock
        elif (user == '1' and comput == 2):
            print("The computer picked Paper \nYou picked Rock \nYou Lose")
        elif (user == '1' and comput == 3):
            print("The computer picked Scissors \nYou picked Rock \nYou Win")

        #User Paper
        elif (user == '2' and comput == 1):
            print("The computer picked Rock \nYou picked Paper \nYou Win")
        elif (user == '2' and comput == 3):
            print("The computer picked Scissors \nYou picked Paper \nYou Lose")

        #User Scissors
        elif (user == '3' and comput == 1):
            print("The computer picked Rock \nYou picked Scissors \nYou Lose")
        elif (user == '3' and comput == 2):
            print("The computer picked Paper \nYou picked Scissors \nYou Win")

        #End the game
        elif (user == 'x' or user == 'X'):
            done = True
            print("End of game, thank you for playing!:)")
        #Error message
        elif((user != '1') or (user != '2') or (user != '3') or (user != 'x') or (user != 'X')):
            print("Error: that is not an option, try again") 
#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************
main()
