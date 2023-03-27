import json
from utilities import hash_string, compare_timestamp
from getpass import getpass
import os.path


def login():
    
    # open json file and load into a list data structure called data
    file = open('users.json', 'r')
    data = json.load(file)
    file.close()

    print("Welcome back to secure drop. Please Login: ")
    
    # 3 Chances at login before application restarts
    for i in range (3, 0, -1):

        # Convert email into hashed version
        print("Enter Email Address:")
        email = input()
        # hash_string(input(), data['Salt'])

        # Convert email into hashed version
        print("Enter Password:")
        password = hash_string(getpass(), data['Salt'])

        # Check if entered hashes match with the data in the derived dictionary
        if email != data['Email'] or password != data['Key']:
            print("\nEmail and Password Combination Invalid")
            print("{} Try(s) left.".format(i-1))
        else:
            break
        
        # limit to 3 tries. Return -1 if unsuccessful
        if i == 1:
            print("Failed to login 3 times. Exiting Program.")
            return 1

     # Check if there has been modifications
    if(os.path.exists("contacts.json")):
        if compare_timestamp("time_log.txt", "contacts.json") == False:
            print("!!!WARNING!!!:Contact has been modified outside of the session!")
        else:
            print("It works....")

    return 0
            

