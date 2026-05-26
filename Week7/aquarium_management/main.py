# Creating the main program to run the following system

# Adding in necesssary imports
from factory import FishFactory
from aquarium import Aquarium

def main():

    aquarium = Aquarium()

    while True:

        print("\n=== Auckland Aquarium ===")
        print ("1. Add Fish")
        print("2. Display Aquarium")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            fish_name = input(
                "Enter fish type (GoldFish, Shark, Angelfish, Tuna, Salmon): "
            )

            fish = FishFactory.create_fish(fish_name)

            if fish:
                aquarium.add_fish(fish)
                print(f"\nAdded: {fish.display_info()}")
            
            else:
                print("Invalid fish type! ")

        elif choice == "2":
            aquarium.display_inventory()

        elif choice == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid Option!")

if __name__ == "__main__":
    main()