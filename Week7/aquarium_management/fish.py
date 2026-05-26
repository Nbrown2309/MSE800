# creating the fish classes

class Fish:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
        return f"{self.name} belongs to {self.category} category."
    
class Goldfish(Fish):
    def __init__(self):
        super().__init__("Goldfish", "Freshwater")

class Shark(Fish):
    def __init__(self):
        super().__init__("Shark", "Saltwater")

class Angelfish(Fish):
    def __init__(self):
        super().__init__("Angelfish", "Freshwater")

class Tuna(Fish):
    def __init__(self):
        super().__init__("Tuna", "Saltwater")

class Salmon(Fish):
    def __init__(self):
        super().__init__("Salmon", "Freshwater/Saltwater")
