class Animal:
    """
    Docstring for Animal
    """
    def __init__(self, species : str = "Default Species", age : int = 0) -> None:
        self._species = species
        self._age = age

    def __str__(self):
        return f"{self._age}-year-old {self._species}"
    
class Pet(Animal):
    """
    Docstring for Pet
    """
    def __init__(self, species : str, age : int, name = "Default Name") -> None:
        super().__init__(species, age) # Invoke Anima's initiazer
        # Let Animal initialize Animal-Specific state
        
        self._name = name

    def __str__(self):
        str_rep = super().__str__()
        str_rep += " named " + self._name

        return str_rep

class WildAnimal(Animal):
    """
    Docstring for WildAnimal
    """
    def __init__(self, species : str, age : int, noise = "Default Noise") -> None:
        super().__init__(species, age) # Invoke Anima's initiazer
        # Let Animal initialize Animal-Specific state
        
        self._noise = noise

    def __str__(self):
        str_rep = super().__str__()
        str_rep += " that goes " + self._noise

        return str_rep


def main():
    dog = Animal("Dog", 2)
    print(dog)

    animal = Animal()
    print(animal)

    max = Pet("Dog", 5, "Max")
    print(max)

    lion = WildAnimal("Lion", 8, "Rawr")
    print(lion)

    print()

    animals = [dog, animal, max, lion]

    for animal in animals:
        print(animal)  # Same code, different behavbior

main()