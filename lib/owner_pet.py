class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        Pet.all.append(self)  # Add this instance to the all list

    def set_owner(self, owner):
        if isinstance(owner, Owner):
            self.owner = owner
        else:
            raise Exception("Owner must be an instance of Owner class.")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.set_owner(self)  # Set the owner of the pet
        else:
            raise Exception("Pet must be an instance of Pet class.")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

