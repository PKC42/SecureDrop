Secure Drop
Team 9
Sidarong Men, Thomas Breau, Pratush Kc
12/13/2022
Milestones 1-5 Submission 

    This program utilizes UDP and TLS protocols to sercurely transfer files over from one computer to another. To accomplish this, several threads are
    run in concurently for live communication between devices. This project was done as a part of Introduction to Computer Security at UMass Lowell.

    In order to use this application, download and run secure_drop.py. If you do not have a certificate already generated, one will be created (one time only).
    Enter your name, email and password. This will be saved in an protected json file. The password will be hashed. Contacts can be added using the add option.
    Each contact requires a name, email and ip address to enable communication via sockets. All online contacts can be seen using the list option. To exit,
    the application, enter "exit" in the main menu. For help, type "help" in the main menu.

    Bugs:
    When sending files, the ssl socket says that it is still in use despite closing the socket and restarting. This has yet to be resolved.
    


    Files:
        secure_drop.py (all major functions are called from here)
        registration.py (handles registration)
        login.py (handles login)
        operation.py (handles operations)
        unit_test.py (used for unit testing)
        utilities.py (contains extra helpful user defined functions)
        users.json (contains user information)
        contacts.json (contains contact information)
        time_log.txt (for checking if there are any changes)
        communications.py (for socket programming (sending and receiving files))



        
