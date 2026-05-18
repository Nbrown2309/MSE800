# app.py to make the whole application run smoothly

from auth import login
from zoo import add_animal, view_animals, remove_animal


def menu():
    while True:
        print("\n===== Zoo Management System =====")
        print("1. Login")
        print("2. Add Animal")
        print("3. View Animals")
        print("4. Remove Animal")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            login()

        elif choice == "2":
            add_animal()

        elif choice == "3":
            view_animals()

        elif choice == "4":
            remove_animal()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid option.")


menu()