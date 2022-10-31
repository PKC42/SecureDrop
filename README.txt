Secure Drop
Team 9
Sidarong Men, Thomas Breau, Pratush Kc
10/31/2022
Milestones 1-3 Submission 

Milestone 1:
    - The program scans for a user.json file.
    - If the user.json file does not exist, a user.json file is created.
        - Once created, the file permissions is set to read only by owner.
        - Pycryptodome is used to hash the email and password.
        - The name, hashed email, hashed password and salt are stored in the user.json file as a dictionary.
        - All instances of plaintext passwords and email are deleted as soon as possible.
    - If the user.json file already exists, the user is prompted to login as described in Milestone 2.


Milestone 2:
    - The user gets 3 tries to get in before the program automatically exits.
        - Password is hidden in the terminal when entering it in.
        - The email and password are immediately hashed.
        - The dictionary stored in users.json is loaded into a dictionary data structure.
        - The entered hashes are compared to the stored hashes.
        - If the hashes don't match, the user is forced to try to login again and 1 attempt is subtracted.
        - If the hashes match, the user is allowed into Secure Drop.

Milestone 3:
    - An operation menu is added in operations.py.
    - For milestone 3, help, exit and add are implemented.
    - Help lists all operations.
    - Exit takes the user out of secure drop effectively ending the program.
    - Add allows the user to add contacts.
    - If add is selected the user is prompted to type in the name of the contact along with email.
        - The contact email is hashed and the salt is saved.
        - The name, hashed email and salt are added to the file (there may be more sensitive fields such as keys added in the future here).
        - The dictionary is a dictionary of dictionaries.
        - The first dictionary contains the names of the users which act as the keys. 
        - The values assigned to the keys are dictionaries which contain the sensitive information and salt.
        - If the first contact is being added, the contacts.json file is created with the permissions changed.
        - Only the owner can read and write into the contacts.json file.
        - The contact is dumped into the json file and saved.
        - If another contact is to be added, the contacts.json file is opened for reading.
        - The data inside is loaded into a variable in the python program.
        - The user is added with the name being the key and the other sensitive information being hashed and added the value in the form of another dictionary.
        - The file is saved. 


    Potential Problems:
        - When registering the user, there is no protections against a bogus file
        - Files can still be deleted in disruption attacks
        - If the owner's account is compromised, the attacker may potentially conduct an injection attack to destroy data.
        - We still do not have a way to detect if a file has been modified by an attacker. 

    To do list:
        - Make sure that json files can not be edited or deleted (may need to revoke all permissions before ending the program).
        - Make sure json files can not be easily deleted.
        - Find a way to detect changed made by an attacker

    Files:
        secure_drop.py (all major functions are called from here)
        registration.py (handles registration)
        login.py (handles login)
        operation.py (handles operations)
        unit_test.py (used for unit testing)
        utilities.py (contains extra helpful user defined functions)
        users.json (contains user information)
        contacts.json (contains contact information)

    For testing: 
        Delete users.json and contacts.json before trying out registration contact addition
        Current login creditials with the submitted data are:
        Name: John Smith 
        Email: john_smith@student.uml.edu
        Password: #Ireallylikeapples1

        
