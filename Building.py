from campus import Campus
from equipment import Equipment

class Building(Campus):
    def __init__(self, building_name="Building", items=None):
        super().__init__(self)

        # Initialialize items list inside object initialization to avoid using the same list across instances
        if items == None:
            items = []
        self.building_name = building_name
        self.items = items

    ### Deleters
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)


    ### Filters
    def filter_by_department(self, department, items=None):
        if not items:
            items = self.get_items()
        return super().filter_by_department(department, items)

    def filter_by_manufacturer(self, manufacturer, items=None):
        if not items:
            items = self.get_items()
        return super().filter_by_manufacturer(manufacturer, items)

    def filter_by_name(self, name, items=None):
        if not items:
            items = self.get_items()
        return super().filter_by_name(name, items)

    def filter_by_room(self, room, items=None):
        if not items:
            items = self.get_items()
        return super().filter_by_room(room, items)


    ### Getters
    def display_items(self, items=None):
        if not items:
            items = self.items
        super().display_items(items, building=False)

    def get_building_name(self):
        return self.building_name

    def get_items(self):
        return self.items


    ### Setters
    def add_item(self, item):
        if isinstance(item, Equipment):
            self.items.append(item)

    def set_items(self, items):
        self.items = items


    ### Sorts
    def sort_by_department(self, items=None):
        if not items:
            items = self.items
        return super().sort_by_department(items)
    
    def sort_by_manufacturer(self, items=None):
        if not items:
            items = self.items
        return super().sort_by_manufacturer(items)

    def sort_by_name(self, items=None):
        if not items:
            items = self.items
        return super().sort_by_name(items)

    def sort_by_room(self, items=None):
        if not items:
            items = self.items
        return super().sort_by_room(items)

    def sort_by_quantity(self, items=None):
        if not items:
            items = self.items
        return super().sort_by_quantity(items)
