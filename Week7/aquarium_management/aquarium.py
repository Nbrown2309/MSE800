# aquarium.py

class Aquarium:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super(Aquarium, cls).__new__(cls)

            cls._instance.inventory = {
                "Goldfish": 0,
                "Shark": 0,
                "Angelfish": 0,
                "Tuna": 0,
                "Salmon": 0
            }

        return cls._instance

# adding in a limit to the number of fish in the aquarium
    def add_fish(self, fish):

        if self.inventory[fish.name] < 3:
            self.inventory[fish.name] += 1
            print(f"{fish.name} added to the aquarium successfully.")

        else:
            print(f"Cannot add more {fish.name}s. Maximum capacity reached.")

    def display_inventory(self):

        print("\nAquarium Fish Inventory")
        print("-" * 30)

        for fish, count in self.inventory.items():
            print(f"{fish}: {count}")