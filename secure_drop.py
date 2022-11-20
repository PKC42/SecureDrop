from registration import register_new_user
from login import login
from utilities import user_file_scan
from operation import operation

def run():
    
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
            print("Welcome to Secure Drop.")
            # functions for list commands go here
            while True:
                print("secure_drop> ")
                user_selection = input()
                status = operation(user_selection)

                # If there is an error witht he input, indicate it as such
                if status == "input_error":
                    print("Input Error. Please choose a valid operation. Type \"help\" to see options")

                # If the return value of operation is 0, we can exit the program.
                if status == "exit":
                    break
            
    print("Exiting Secure Drop.")
    return
    
if __name__ == "__main__":
    run()