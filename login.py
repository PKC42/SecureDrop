

def login():
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

