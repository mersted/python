# This program randomly generates any number of names
# The program has a pre-set list of first and last names,
# but the user can add any appropriate name of their 
# choosing to either list

# The program uses the string module to check to see
# if a user-inputted name is an acceptable name
# and the random module to help generate a random name


from random import *
from string import *


# Main function
def main():
    
    # Asks user how many names they want to generate
    num_names = integer_check("How many names do you want to generate?")
    
    # listOfNames() returns two lists of names, which are assigned to
    # fn and ln (first name and last name)
    fn, ln = listOfNames()
    
    # generateNames() returns a list of full names
    list_names = generateNames(fn, ln, num_names)
    
    # printNames() prints the list of names
    printNames(list_names, num_names)



# Function that creates list of first and last names
# Allows user to make additions to either list
def listOfNames():
    # Initial lists of first and last names
    first_names = ["Matt", "Mike", "Mert", "Clifton", "Thorbjorn", "Charles", "Sherlock", "Christian"]
    last_names = ["Johnson", "Smith", "Aliadiere", "Elyounoussi", "Chiriches", "Sigurdsson", "Eriksen", "Holmes"]

    print("\nThe current list of first names:")
    print(first_names)
    print("\nThe current list of last names:")
    print(last_names)
    
    # Asks user if they want to add names to list of first names
    ans_one = input("Would you like to add any first names to the list? (yes/no)")
    
    if ans_one == "yes":
    
        num_added_names = integer_check("How many first names do you want to add?")
        
        i = 0
        
        while i < num_added_names:
        
            new_first_name = input("Enter name:")
            
            # Check to see if name is acceptable
            # checkName() returns either True or False
            if checkName(new_first_name):
            
                # .title() capitalizes first letter of name
                first_names.append(new_first_name.title())
                
                i += 1
                
            else:
                continue
    
    # Asks user if they want to add names to list of last names
    ans_three = input("Would you like to add any last names to the list? (yes/no)")
    
    if ans_three == "yes":
    
        num_added_names_1 = integer_check("How many last names do you want to add?")
        
        n = 0
        
        while n < num_added_names_1:
        
            new_last_name = input("Enter name:")
            
            if checkName(new_last_name):
            
                last_names.append(new_last_name.title())
                
                n += 1
            
            else:
                continue


    return first_names, last_names


# Generates the randomized names
# Creates a list of the names created
def generateNames(firstn, lastn, num):
    
    list_of_names = []
    
    for x in range(num):
    
        # How many names in the list
        maximum_first = len(firstn)
        maximum_last = len(lastn)
        
        # Gets a random number 
        num_one = randint(0, maximum_first)
        num_two = randint(0, maximum_last)
        
        # Uses random number as index, to find
        # name in list
        random_first = firstn[num_one - 1]
        random_last = lastn[num_two - 1]

        # Concatenates first and last name with a space
        random_full_name = random_first + " " + random_last
        
        # Adds name to the list
        list_of_names.append(random_full_name)

    return list_of_names




# Prints the list of names generated
def printNames(theList, theNum):

    num_of_names = str(theNum)

    print("\nYour " + num_of_names + " randomly generated names:\n")
    
    # Iterates through the list of randomly generate names and prints
    for x in theList:
        print(x)

    print("\n")


# Checks to see if user-inputted name is an acceptable name
def checkName(nameStr):
    
    name = True
    
    # Sets the characters for an acceptable name as any
    # letter, hypen, apostrophe, or white space
    acceptable_letters = ascii_letters + "-'" + whitespace
    
    for x in nameStr:
        if x not in acceptable_letters:
            print("Not an acceptable name, try again")
            name = False
            return
    
    return name



# Try to change value inputted into an int
# If not a valid integer, asks again
# Uses a try except, infinite while loop
def integer_check(theString):

    while True:
        try:
            x = int(input(theString))
            break
        except:
            print("Not a valid integer")
    
    return x
