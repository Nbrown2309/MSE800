"""
Log in and signup System 

This program allows users to:
- create an account (sign up)
- log in to their account
- reset their password if they forget it
- manage their account information
"""

from services.auth_service import AuthService

# Create an instance of the AuthService class to handle authentication
auth = AuthService()

# Start the main loop of the application
while True:

# Making the UI for the login system
    print("\n===== LOGIN SYSTEM =====")
    print("1. Sign Up")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        auth.signup()

    elif choice == "2":
        auth.login()

    elif choice == "3":
        auth.forgot_password()

    elif choice == "4":
        print("Goodbye, Have a nice day!")
        break

    else:
        print("Invalid Option")
