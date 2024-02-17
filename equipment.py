class Equipment:
    def __init__(self, item_name="Item", room_quantity={}, department=["TEST"], manufacturer="Debug", description="This is a test item."):
        self.item_name = item_name
        self.room_quantity = room_quantity
        self.department = department
        self.manufacturer = manufacturer
        self.description = description
        self.from_building = None

    def set_item_name(self, name):
        self.item_name = name

    def get_item_name(self):
        return self.item_name
    
    def set_room_quantity(self, room_quantity):
        if isinstance(room_quantity, dict):
            self.room_quantity = room_quantity

    def get_room_quantity(self):
        return self.room_quantity
    
    def add_room(self, room, quantity):
        if isinstance(room, str) and isinstance(quantity, int):
            self.room_quantity[room] = quantity

    def remove_room(self, room):
        if room in self.room_quantity:
            del self.room_quantity[room]

    def set_quantity_of_room(self, room, quantity):
        if room in self.room_quantity and isinstance(quantity, int):
            self.room_quantity[room] = quantity
    
    def get_quantity_of_room(self, room):
        if room in self.room_quantity:
            return self.room_quantity[room]
        
    def inc_room_quantity(self, room):
        if room in self.room_quantity:
            self.room_quantity[room] = self.room_quantity[room] + 1

    def dec_room_quantity(self, room):
        if room in self.room_quantity:
            if self.room_quantity[room] > 0:
                self.room_quantity[room] = self.room_quantity[room] - 1
    
    def get_total_quantity(self):
        total_quantity = 0
        for room in list(self.room_quantity.keys()):
            total_quantity += self.room_quantity[room]
        return total_quantity
    
    def set_department(self, department):
        if isinstance(department, list):
            self.department = department
    
    def get_department(self):
        return self.department
    
    def add_department(self, department):
        if isinstance(department, str):
            self.department.append(department)
    
    def remove_department(self, department):
        if department in self.department:
            self.department.remove(department)

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer
    
    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
    
    def set_from_building(self, building):
        self.from_building = building

    def get_from_building(self):
        return self.from_building