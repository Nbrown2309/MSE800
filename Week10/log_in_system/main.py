from services.auth_service import AuthService

auth = AuthService()

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