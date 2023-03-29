from registration import register_new_user
from login import login
from utilities import user_file_scan
from utilities import *
from operation import operation
from threading import Thread
from communications import *
import threading


def run():

    # flag for ending threads
    end_flag = threading.Event()

    # If user file does not exist, register to create a user
    if user_file_scan() == False:
        print("No users are registered with this client.")
        print("Do you want to register a new user (y/n)?")

        # Prompt user to choose whether to register a new user or not
        while True:
            selection = input()
            selection = selection.lower()
            if selection == 'y' or selection == 'n':
                break
            else:
                print("Error: Invalid input.")
                print("Do you want to register a new user (y/n)?")

        # If yes, register the new user and exit secure drop, else just exit secure drop
        if selection == 'y':
            register_new_user()
            print("Exiting Secure Drop")
            return
        else:
            print("Exiting Secure Drop.")
            return
    else:
        # if login == 1 (unsuccessful), exit secure drop. Else, enter secure drop
        if login() == 1:
            print("Exiting Secure Drop.")
            return
        else:
            # pass a list which will be updates in thread 2
            online_user_emails = []

            # start broadcasting that the client is now online
            if contact_file_scan() == True:
                t1 = Thread(target = broadcast, args = (end_flag, ))
                t1.start() 

            t2 = Thread(target = listen, args = (end_flag, online_user_emails))
            t2.start()

            print("Welcome to Secure Drop.")
            # functions for list commands go here
            while True:
                print("secure_drop> ")
                user_selection = input()
                status = operation(user_selection, online_user_emails)

                # If there is an error with he input, indicate it as such
                if status == "input_error":
                    print("Input Error. Please choose a valid operation. Type \"help\" to see options")

                # If the return value of operation is 0, we can exit the program.
                if status == "exit":
                    break
            
    print("Exiting Secure Drop.")
    end_flag.set()

    return
    
if __name__ == "__main__":
    run()