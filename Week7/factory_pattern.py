from abc import ABC, abstractmethod

# -----------------------
# Product (Abstract Class)
# -----------------------
class Animal(ABC):

    @abstractmethod
    def run(self):
        pass


# -----------------------
# Concrete Products
# -----------------------
class Dog(Animal):
    def run(self):
        print("I'm a Dog, I can run!!")


class Cat(Animal):
    def run(self):
        print("I'm a Cat, I can run!!")


# -----------------------
# Factory (Abstract)
# -----------------------
class Factory(ABC):

    @abstractmethod
    def create_product(self, kind=None):
        pass


# -----------------------
# Concrete Factory
# -----------------------
class AnimalFactory(Factory):

    def create_product(self, kind=None):
        if kind == "dog":
            return Dog()
        elif kind == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


# -----------------------
# Client Code (How you use it)
# -----------------------

factory = AnimalFactory()

dog = factory.create_product("dog")
dog.run()

cat = factory.create_product("cat")
cat.run()