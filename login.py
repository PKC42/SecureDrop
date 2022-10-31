import json
from utilities import hash_string

def login():

    '''
    file = open('', "rb")

    while True:

        print("Enter Email Address:")
        email_user = input()

        print("Enter Password:")
        password_user = input()

        if email_user == email and password_user == password:
            break
        else:
            print("Email and Password Combination Invalid.")

    print("Welcome to SecureDrop.")
    print("Type 'help' for Commands")
    
    '''
    # open json file and load into a list data structure called data
    file = open('users.json', 'r')
    data = json.load(file)
    file.close()

    # 3 Chances at login before application restarts
    for i in range (3, 0, -1):

        # Convert email into hashed version
        print("Enter Email Address:")
        email = hash_string(input(), data['Salt'])

        # Convert email into hashed version
        print("Enter Password:")
        password = hash_string(input(), data['Salt'])

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


    return 0
            

