# This is the auth.py which shows to logging into the zoo app

# auth.py

logged_in = False


def login():
    global logged_in

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == "admin" and password == "zoo123":
        logged_in = True
        print("\nLogin successful!\n")
    else:
        print("\nInvalid username or password.\n")


def admin_required(func):
    def wrapper(*args, **kwargs):
        if logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login first.")
    return wrapper