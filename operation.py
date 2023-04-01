import re
from utilities import check_lower, check_upper, check_number, check_symbol, get_timestamp, hash_string
from utilities import online_user_emails
import json
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from pathlib import Path
from os.path import exists
import os, sys, stat
import datetime, time
from communications import send_file, receive_file


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
        send()
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

    # del contact_email

    status = "Offline"
      
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
            "Email" : contact_email,
            "Salt": salt,
            "IP": ip_address,
            "Status": status
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
                "Email" : contact_email,
                "Salt": salt,
                "IP" : ip_address,
                "Status" : status
                }
        }
        json.dump(contact_data, fp)
        fp2.write("Start")
        fp.close()
        fp2.close()
        
        print("Contact Added")


def list():

    file = Path('contacts.json')
    if file.is_file():
        pass
    else:
        print("No Contacts!")

    print("Online Contacts: ")
    for item in online_user_emails:
        print(item)


    print("\n")
    


def send():

    status = False

    while status == False:
        print("Who do you want to send the file to?")
        contact = input()
        file = Path('contacts.json')

        if file.is_file():
            fp = open('contacts.json', "r")
            data = json.load(fp)
            for contacts in data:
                if contact == contacts:
                    status = True
            if status == False:
                print(contact, " is not in your contacts list! Please enter a valid contact!")
        else:
            print("No Contacts! Returning to main menu.")
            return

    print("Enter the file that you want to send (include path if it is not in the program folder)")
    file_name = input()
    file = Path(file_name)
    while file.is_file() == False:
        print("Unable to get file. Try again.")
        file_name = input()
        file = Path(file_name)
    
    print(f"{file_name} is a valid file!")

    ip_address = data[contact]["IP"]

    print("This is the ip of your contact:", ip_address)
    # send_file(ip_address , file_name)


    
    
