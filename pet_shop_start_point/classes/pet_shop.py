class PetShop:

    def __init__(self, name, pets, cash):
        self.name = name
        self.pets = pets
        self.total_cash = cash
        self.pets_sold = 0

    def stock_count(self):
       return len(self.pets)
    
    def increase_pets_sold(self):
       self.pets_sold += 1
    
    
    def increase_total_cash(self, amount):
        self.total_cash += 500
    
    def add_pet(self, new_pet):
        new_pet = ("Lancelot", "dog", "Basset Hound", 750)
        self.pets.append(new_pet)
    
    def remove_pet(self, pet_to_remove):
        self.pets.remove(pet_to_remove)
    
    def find_pet_by_name(self, pet_name_to_look_for):
        for pet in self.pets:
            if pet.name == pet_name_to_look_for:
                return pet

    def sell_pet_to_customer(self, pet_name, customer):
        pet_to_sell = self.find_pet_by_name(pet_name)
        customer.add_pet(pet_to_sell)
        self.remove_pet(pet_to_sell)
        self.increase_pets_sold()
        pet_price = pet_to_sell.price
        self.increase_total_cash(pet_price)