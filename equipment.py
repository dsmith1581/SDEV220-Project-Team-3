# Project Team 3 (Alexander Smith, Daniel Smith, John Sharp)
# Ivy Tech Asset Manager - Equipment class
# Implements the equipment class which allows creating objects which represent assets in a given location

import validations


class Equipment:
    def __init__(self, item_name="Item", room_quantity={}, department=["TEST"], manufacturer="Debug", description="This is a test item."):
        # Re-uses setter functions to avoid duplicating validation logic
        self.set_item_name(item_name)
        self.set_room_quantity(room_quantity)
        self.set_department(department)
        self.set_manufacturer(manufacturer)
        self.set_description(description)
        self.set_from_building(None)


    ### Deleters
    def remove_department(self, department):
        if department in self.department:
            self.department.remove(department)

    def remove_room(self, room):
        if room in self.room_quantity:
            del self.room_quantity[room]


    ### Getters
    def get_department(self):
        return self.department

    def get_description(self):
        return self.description

    def get_from_building(self):
        return self.from_building

    def get_item_name(self):
        return self.item_name

    def get_manufacturer(self):
        return self.manufacturer

    def get_room_quantity(self):
        return self.room_quantity

    def get_total_quantity(self):
        total_quantity = 0
        for room in list(self.room_quantity.keys()):
            total_quantity += self.room_quantity[room]
        return total_quantity

    def get_quantity_of_room(self, room):
        if room in self.room_quantity:
            return self.room_quantity[room]


    ### Setters
    def add_department(self, department):
        if isinstance(department, str):
            self.department.append(department)
        else:
            raise ValueError(f"Department {department} is an invalid value")

    def add_room(self, room, quantity):
        if isinstance(room, str) and isinstance(quantity, int):
            self.room_quantity[room] = quantity

    def set_department(self, department):
        if not validations.has_valid_characters(department):
            raise ValueError(f"Item department '{department}' contains invalid characters")
        # TODO: this check breaks the current test.py. Need to validate it is creating the departments before trying to assign them or change the way this logic works to do that automatically
        #if isinstance(department, list):
        self.department = department


    def set_description(self, description):
        if not validations.has_valid_characters(description):
            raise ValueError(f"Item description '{description}' contains invalid characters")
        self.description = description

    def set_from_building(self, building):
        self.from_building = building

    def set_item_name(self, name):
        if not validations.has_valid_characters(name):
            raise ValueError(f"Item name '{name}' contains invalid characters")
        self.item_name = name

    def set_manufacturer(self, manufacturer):
        if not validations.has_valid_characters(manufacturer):
            raise ValueError(f"Item manufacturer '{manufacturer}' contains invalid characters")
        self.manufacturer = manufacturer
    
    def set_room_quantity(self, room_quantity):
        if isinstance(room_quantity, dict):
            self.room_quantity = room_quantity

    def set_quantity_of_room(self, room, quantity):
        if room in self.room_quantity and isinstance(quantity, int):
            self.room_quantity[room] = quantity


    ### Updaters
    def dec_room_quantity(self, room):
        if room in self.room_quantity:
            if self.room_quantity[room] > 0:
                self.room_quantity[room] = self.room_quantity[room] - 1

    def inc_room_quantity(self, room):
        if room in self.room_quantity:
            self.room_quantity[room] = self.room_quantity[room] + 1

    
