# adding in the zoo py for the following animals
# zoo.py

from auth import admin_required

animals = []


@admin_required
def add_animal():
    animal = input("Enter animal name: ")
    animals.append(animal)
    print(f"{animal} added to the zoo.")


@admin_required
def view_animals():
    if len(animals) == 0:
        print("No animals in the zoo.")
    else:
        print("\nZoo Animals:")
        for animal in animals:
            print("-", animal)


@admin_required
def remove_animal():
    animal = input("Enter animal name to remove: ")

    if animal in animals:
        animals.remove(animal)
        print(f"{animal} removed from the zoo.")
    else:
        print("Animal not found.")