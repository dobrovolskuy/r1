class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Mammal(Animal):
    def __init__(self, name, species, diet_type):
        super().__init__(name, species)
        self.diet_type = diet_type

    def display_info(self):
        super().display_info()
        print(f"Diet_type:{self.diet_type}")


class Carnivore(Mammal):
    def __init__(self, name, species, diet_type, teeth_count ):
        super().__init__(name, species, diet_type)
        self.teeth_count= teeth_count

    def display_info(self):
        super().display_info()
        print(f"Teeth_count:{self.teeth_count}")

class Lion(Carnivore):
    def __init__(self, name, species, diet_type, teeth_count, mane_size):
        super().__init__(name, species, diet_type, teeth_count)
        self.mane_size = mane_size

animal = Animal(name="Generic Animal", species="Unknown")
animal.display_info()

mammal = Mammal(name="Generic Mammal", species="Unknown", diet_type="Omnivore")
mammal.display_info()

carnivore = Carnivore(name="Generic Carnivore", species="Unknown", diet_type="Carnivore", teeth_count=32)
carnivore.display_info()

lion = Lion(name="Simba", species="Lion", diet_type="Carnivore", teeth_count=30, mane_size="Large")
lion.display_info()