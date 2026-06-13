# Creating the class for the user
class User:

    def __init__(self, full_name, dob, email, password):
        self.full_name = full_name
        self.dob = dob
        self.email = email
        self.password = password

    def display_profile(self):
        print("\n --- User Profile ---")
        print(f"Name: {self.full_name}")
        print(f"DOB: {self.dob}")
        print(f"Email: {self.email}")

    def update_profile(self, new_name, new_dob):
        self.full_name = new_name
        self.dob = new_dob

    def change_password(self, new_password):
        self.password = new_password