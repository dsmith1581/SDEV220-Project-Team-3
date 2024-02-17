# Project Team 3 (Alexander Smith, Daniel Smith, John Sharp)
# Ivy Tech Asset Manager - Campus class
# Implements the Campus class which is the root view of an asset inventory.

import validations


class Campus:
    # TODO - is location actually a string or a building object?
    def __init__(self, location="Somewhere", id="501", buildings=None):
        # Re-uses setter functions to avoid duplicating validation logic
        self.location = location
        self.set_id(id)
        if buildings == None:
            self.set_buildings([])
        else:
            self.set_buildings(buildings)
        self.sorted_quantity = False
        self.sorted_name = False
        self.sorted_department = False
        self.sorted_manufacturer = False
        self.sorted_room = False


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

    def set_id(self, id):
        if not validations.has_valid_characters(id):
            raise ValueError(f"New campus id '{id}' contains invalid characters")
        self.id = id


    ### Sorts
    def toggle_department_sort(self):
        self.sorted_quantity = False
        self.sorted_name = False
        self.sorted_room = False
        self.sorted_manufacturer = False
        if self.sorted_department:
            self.sorted_department = False
        else:
            self.sorted_department = True

    def toggle_manufacturer_sort(self):
        self.sorted_quantity = False
        self.sorted_name = False
        self.sorted_department = False
        self.sorted_room = False
        if self.sorted_manufacturer:
            self.sorted_manufacturer = False
        else:
            self.sorted_manufacturer = True

    def toggle_name_sort(self):
        self.sorted_quantity = False
        self.sorted_department = False
        self.sorted_room = False
        self.sorted_manufacturer = False
        if self.sorted_name:
            self.sorted_name = False
        else:
            self.sorted_name = True
    
    def toggle_quantity_sort(self):
        self.sorted_name = False
        self.sorted_department = False
        self.sorted_room = False
        self.sorted_manufacturer = False
        if self.sorted_quantity:
            self.sorted_quantity = False
        else:
            self.sorted_quantity = True
    
    def toggle_room_sort(self):
        self.sorted_quantity = False
        self.sorted_name = False
        self.sorted_department = False
        self.sorted_manufacturer = False
        if self.sorted_room:
            self.sorted_room = False
        else:
            self.sorted_room = True

    def sort_by_department(self, items = None):
        if not items:
            items = self.get_all_items_campus()
        if self.sorted_department:
            filtered_items = sorted(items, key=lambda x: x.department[0], reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: x.department[0], reverse=False)
        self.toggle_department_sort()
        return filtered_items

    def sort_by_manufacturer(self, items = None):
        if not items:
            items = self.get_all_items_campus()
        if self.sorted_manufacturer:
            filtered_items = sorted(items, key=lambda x: x.manufacturer, reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: x.manufacturer, reverse=False)
        self.toggle_manufacturer_sort()
        return filtered_items

    def sort_by_name(self, items = None):
        if not items:
            items = self.get_all_items_campus()
        if self.sorted_name:
            filtered_items = sorted(items, key=lambda x: x.get_item_name(), reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: x.get_item_name(), reverse=False)
        self.toggle_name_sort()
        return filtered_items

    def sort_by_room(self, items = None):
        if not items:
            items = self.get_all_items_campus()
        if self.sorted_room:
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
        if self.sorted_quantity:
            filtered_items = sorted(items, key=lambda x: x.get_total_quantity(), reverse=True)
        else:
            filtered_items = sorted(items, key=lambda x: x.get_total_quantity(), reverse=False)
        self.toggle_quantity_sort()
        return filtered_items
