import re
from utilities import check_lower, check_upper, check_number, check_symbol, hash_string
import json
import hashlib
import os

# This folder will contain the user registration processes

def register_new_user():
    print("Enter Full Name:")
    # Name Validity Check
    while True:
        name = input()
        if re.match(r'^[aA-zZ]+$', name):
            break
        else:
            print("Invalid Input. Name must have a charactar.")
    
        
    print("Enter email address:")
    while True:
        email = input()
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            break
        else:
            print("Please enter a valid email with format: local-part@domain")


    while True:
             
        print("Enter a new password:")
        while True:
            password_1 = input()
            if len(password_1) >= 4 and check_lower(password_1) and check_upper(password_1) and check_number(password_1) and check_symbol(password_1):
                break
            print("Password must be at least 16 character, contain at least 1 lowercase letter, and 1 uppercase letter, and 1 special character")
            
            
        print("Re-enter password:")
        password_2 = input()

        if password_1 == password_2:
            password = password_1
            break 
        else:
            print("Password must match. Please retry creating a password!")

    print("Passwords Match.")
    print("User Registered.")

    # Hash 
    salt = os.urandom(32)
    hashed_name = hash_string(name, salt)
    hashed_email = hash_string(email, salt)
    hashed_pass = hash_string(password, salt)
    
    storage = salt + hashed_pass
    #s = storage.decode()

    data = {
        "Name:": hashed_name,
        "Email": hashed_email,
        "Key" : hashed_pass
    }

    #Writes user data into text file 
    with open("users.txt", "w") as outfile:
        outfile.write("Name: ")

    with open("users.txt", "ab") as outfile:
        outfile.write(hashed_name)
    
    with open("users.txt", "a") as outfile:
        outfile.write("\nEmail: ")

    with open("users.txt", "ab") as outfile:
        outfile.write(hashed_email)

    with open("users.txt", "a") as outfile:
        outfile.write("\nPassword: ")

    with open("users.txt", "ab") as outfile:
        outfile.write(hashed_pass)

    #Stores salt into key.txt file
    with open("key.txt", "wb") as outfile:
        outfile.write(salt)
    
        