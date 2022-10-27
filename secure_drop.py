from registration import register_new_user


# number of users (temporary placeholder for file scan)
userCount = 0

if userCount == 0:
    print("No users are registered with this client.")
    print("Do you want to register a new user (y/n)?")
    # call registration function from registration.py
    
    while True:
        selection = input()
        selection = selection.lower()
        if selection == 'y' or selection == 'n':
            break
        else:
            print("Error: Invalid input.")
            print("Do you want to register a new user (y/n)?")

    if selection == 'y':
        register_new_user()
    else:
        print("Exiting Secure Drop")
else:
    # call login function from login.py
    pass


    