class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string")
        self.name = name
        self._pets = []  

    def pets(self):
        """Returns a list of all pets owned by the owner."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner's collection if it's a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a list of pets sorted by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}")
        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if owner:
            owner.add_pet(self) 
