import json
import os

class AuthService:

    def __init__(self):
        self.users = {}
        if not os.path.exists("database"):
            os.makedirs("database")
        self.load_users()

    def signup(self):
        email = input("Email: ")

        if email in self.users:
            print("Account already exists.")
            return

        full_name = input("Full Name: ")
        dob = input("Date of Birth: ")
        password = input("Password: ")

        self.users[email] = {
            "name": full_name,
            "dob": dob,
            "password": password
        }

        self.save_users()

        print("Signup Successful!")

    def login(self):
        email = input("Email: ")
        password = input("Password: ")

        if email in self.users and self.users[email]["password"] == password:
            print("Login Successful!")
        else:
            print("Invalid Login")

    def forgot_password(self):
        email = input("Registered Email: ")

        if email not in self.users:
            print("Account not found.")
            return

        dob = input("Enter DOB: ")

        if dob == self.users[email]["dob"]:
            new_password = input("New Password: ")
            self.users[email]["password"] = new_password
            self.save_users()
            print("Password Reset Successful!")
        else:
            print("Verification Failed")

    def save_users(self):
        with open("database/users.json", "w") as file:
            json.dump(self.users, file, indent=4)

    def load_users(self):
        try:
            with open("database/users.json", "r") as file:
                self.users = json.load(file)
        except:
            self.users = {}