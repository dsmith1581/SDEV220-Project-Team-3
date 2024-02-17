class Campus:
    def __init__(self, location="Somewhere", id="501", buildings=None):
        self.location = location
        self.id = id
        if buildings == None:
            self.buildings = []
        else:
            self.buildings = buildings
        self.sortedQuantity = False
        self.sortedName = False
        self.sortedDepartment = False
        self.sortedManufacturer = False
        self.sortedRoom = False

    ### Deleters
    def remove_building(self, building):
        if building in self.buildings:
            self.buildings.remove(building)

    ### Filters
    def filter_by_department(self, department, items=None):
        if not items:
            items = self.get_all_items_campus()
        filtered_items = [x for x in items if department.upper() in x.department]
        return filtered_items

    def filter_by_manufacturer(self, manufacturer, items=None):
        if not items:
            items = self.get_all_items_campus()
        filtered_items = [x for x in items if manufacturer.lower() in x.manufacturer.lower()]
        return filtered_items

    def filter_by_name(self, name, items=None):
        if not items:
            items = self.get_all_items_campus()
        filtered_items = [x for x in items if name.lower() in x.item_name.lower()]
        return filtered_items

    def filter_by_room(self, room, items=None):
        if not items:
            items = self.get_all_items_campus()
        filtered_items = [x for x in items if room.upper() in list(x.room_quantity.keys())]
        return filtered_items


    ### Getters
    def display_items(self, items=None, building=True):
        if not items:
            items = self.get_all_items_campus()
        for item in items:
            if building:
                displayString = "Building: %s\nItem Name: %s\n"
            else:
                displayString = "Item Name: %s\n"
            for room in list(item.room_quantity.keys()):
                displayString += "Room " + room + ": " + str(item.get_quantity_of_room(room)) + "\n"
            displayString += "Total Quantity: %d\nDepartments: %s\nManufacturer: %s\nDescription: %s\n=========="
            if building:
                print(displayString%(item.get_from_building(), item.get_item_name(), item.get_total_quantity(), item.get_department(), item.get_manufacturer(), item.get_description()))
            else:
                print(displayString%(item.get_item_name(), item.get_total_quantity(), item.get_department(), item.get_manufacturer(), item.get_description()))

    def get_all_items_campus(self):
        campus_items = []
        for building in self.buildings:
            for item in building.get_items():
                item.set_from_building(building.get_building_name())
                campus_items.append(item)
        return campus_items

    def get_building(self, name=None):
        if name:
            return [x for x in self.get_buildings() if name.lower() in x.get_building_name().lower()][0]
        else:
            return self.get_buildings()[0]

    def get_buildings(self):
        return self.buildings

    def get_location(self):
        return self.location

    def get_id(self):
        return self.id


    ### Setters
    def add_building(self, building):
        self.buildings.append(building)

    def set_buildings(self, buildings):
        if isinstance(buildings, list):
            self.buildings = buildings


    ### Sorts
    def toggle_department_sort(self):
        self.sortedQuantity = False
        self.sortedName = False
        self.sortedRoom = False
        self.sortedManufacturer = False
        if self.sortedDepartment:
            self.sortedDepartment = False
        else:
            self.sortedDepartment = True

    def toggle_manufacturer_sort(self):
        self.sortedQuantity = False
        self.sortedName = False
        self.sortedDepartment = False
        self.sortedRoom = False
        if self.sortedManufacturer:
            self.sortedManufacturer = False
        else:
            self.sortedManufacturer = True

    def toggle_name_sort(self):
        self.sortedQuantity = False
        self.sortedDepartment = False
        self.sortedRoom = False
        self.sortedManufacturer = False
        if self.sortedName:
            self.sortedName = False
        else:
            self.sortedName = True
    
    def toggle_quantity_sort(self):
        self.sortedName = False
        self.sortedDepartment = False
        self.sortedRoom = False
        self.sortedManufacturer = False
        if self.sortedQuantity:
            self.sortedQuantity = False
        else:
            self.sortedQuantity = True
    
    def toggle_room_sort(self):
        self.sortedQuantity = False
        self.sortedName = False
        self.sortedDepartment = False
        self.sortedManufacturer = False
        if self.sortedRoom:
            self.sortedRoom = False
        else:
            self.sortedRoom = True

    def sort_by_department(self, items = None):
        if not items:
            items = self.get_all_items_campus()
        if self.sortedDepartment:
            filtered_items = sorted(items, key=lambda x: x.department[0], reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: x.department[0], reverse=False)
        self.toggle_department_sort()
        return filtered_items

    def sort_by_manufacturer(self, items = None):
        if not items:
            items = self.get_all_items_campus()
        if self.sortedManufacturer:
            filtered_items = sorted(items, key=lambda x: x.manufacturer, reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: x.manufacturer, reverse=False)
        self.toggle_manufacturer_sort()
        return filtered_items

    def sort_by_name(self, items = None):
        if not items:
            items = self.get_all_items_campus()
        if self.sortedName:
            filtered_items = sorted(items, key=lambda x: x.get_item_name(), reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: x.get_item_name(), reverse=False)
        self.toggle_name_sort()
        return filtered_items

    def sort_by_room(self, items = None):
        if not items:
            items = self.get_all_items_campus()
        if self.sortedRoom:
            filtered_items = sorted(items, key=lambda x: list(x.room_quantity.keys())[0], reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: list(x.room_quantity.keys())[0], reverse=False)
        self.toggle_room_sort()
        return filtered_items

    def sort_by_quantity(self, items = None):
        for x in range(50):
            print(items)
        if not items:
            items = self.get_all_items_campus()
        if self.sortedQuantity:
            filtered_items = sorted(items, key=lambda x: x.get_total_quantity(), reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: x.get_total_quantity(), reverse=False)
        self.toggle_quantity_sort()
        return filtered_items
