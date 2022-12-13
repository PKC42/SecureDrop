import re
from utilities import check_lower, check_upper, check_number, check_symbol, get_timestamp, hash_string
import json
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from pathlib import Path
import os, sys, stat
import datetime, time


# contains operations list once the user logs in
def operation(menu_option):

    # display help menu
    if(menu_option == "help"):
        help()
        return "done"
    
    # add contact
    elif(menu_option == "add"):
        add_contact()
        return "done"
    
    # list contacts
    elif(menu_option == "list"):
        #Call list function to print out list of contacts
        list()
        return "done"

    # send files
    elif(menu_option == "send"):
        return "done"
    
    # exit menu
    elif(menu_option == "exit"):
        print("\n")
        return "exit"

    # return "input_error" indicates an error with input
    return "input_error"
    
# help menu
def help():
    print("\"add\"  -> Add a new contact")
    print("\"list\" -> List all online contacts")
    print("\"send\" -> Transfer file to contact")
    print("\"exit\"  -> Exit SecureDrop")
    return

# process for adding contacts
def add_contact():
    print("Enter Full Name: ")

    while True:
        contact_name = input()
        if re.match(r'\b([A-Z]{1}[a-z]+) ([A-Z]{1}[a-z]+)\b', contact_name):
            break
        else:
            print("Invalid Input. Contact name must be entered with format Firstname Lastname (Capitalize first letter of each part).")
    
    print("Enter email address:")
    while True:
        contact_email = input()
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', contact_email):
            break
        else:
            print("Please enter a valid email with format: local-part@domain")
    
    salt = get_random_bytes(16)
    salt = salt.decode("ISO-8859-1")

    hashed_contact_email = hash_string(contact_email, salt)

    del contact_email
      
    print("Enter IP address of the contact (IPV4): ")
    while True:
        ip_address = input()
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip_address):
            break
        else:
            print("Enter an IPV4 ip address in the correct format.")


  
    file = Path('contacts.json')
    if file.is_file():
        # if file exists, load
        fp = open('contacts.json', 'r')
        fp2 = open('time_log.txt' , 'w')
        # change permissions to read and write
        os.chmod('contacts.json', 0o600)
        data = json.load(fp)
        fp.close()
        data[contact_name] = {
            "Email" : hashed_contact_email,
            "Salt": salt,
            "IP": ip_address
        }
        
        fp = open('contacts.json', 'w')
        fp2.write("Stamp")
        json.dump(data, fp)
        fp.close()
        fp2.close()
        print("Contact Added")

        # change to read only
        os.chmod('contacts.json', 0o400)

    else:
        # init json file
        fp = open('contacts.json', 'w')
        fp2 = open('time_log.txt' , 'w')
        os.chmod('contacts.json', 0o600)
        contact_data = {
            contact_name: {
                "Email" : hashed_contact_email,
                "Salt": salt,
                "IP" : ip_address
                }
        }
        json.dump(contact_data, fp)
        fp2.write("Start")
        fp.close()
        fp2.close()
        
        print("Contact Added")

    
    

def list():
    # contact should only appear if they exist in contacts.json, they other contact has added you and if the other contact is also online

    pass
    

    
def send():
    # select contact to send to (they must be online)

    # send certificate for validation

    # receive certificate 

    
    pass
