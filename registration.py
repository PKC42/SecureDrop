import re
from utilities import check_lower, check_upper, check_number, check_symbol, hash_string
import json
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
'''
import hashlib
import os
'''


# This folder will contain the user registration processes

def register_new_user():
    print("Enter Full Name:")

    # Name Validity Check
    while True:
        name = input()
        if re.match(r'\b([A-Z]{1}[a-z]+) ([A-Z]{1}[a-z]+)\b', name):
            break
        else:
            print("Invalid Input. Name must be entered with format Firstname Lastname (Capitalize first letter of each part).")
    
    # Email Validity Check
    print("Enter email address:")
    while True:
        email = input()
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            break
        else:
            print("Please enter a valid email with format: local-part@domain")

    # Password Validity Check
    while True:
        print("Enter a new password:")
        while True:
            password_1 = input()
            if len(password_1) >= 16 and check_lower(password_1) and check_upper(password_1) and check_number(password_1) and check_symbol(password_1):
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

    # hash 
    '''
    salt = os.urandom(32)
    hashed_name = hash_string(name, salt)
    hashed_email = hash_string(email, salt)
    hashed_pass = hash_string(password, salt)
    
    #storage = salt + hashed_pass
    #s = storage.decode()
    '''

    # generate salt
    salt = get_random_bytes(16)
    salt = salt.decode("ISO-8859-1")

    # hash the email and password
    hashed_email = hash_string(email, salt)
    hashed_pass = hash_string(password, salt)

    # delete all instances of plaintext versions of confidential info
    del email
    del password
    del password_1
    del password_2
    
    # insert into dictionary 
    data = {
        "Name:": name,
        "Email": hashed_email,
        "Key" : hashed_pass,
        "Salt": salt
    }
    '''
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
    '''

    # write into json file
    file = open('users.json', 'w')
    json.dump(data, file)
    file.close()