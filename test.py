from FileManager import FileManager
from Campus import Campus
from Building import Building
from Equipment import Equipment

file_manager = FileManager()
Ivy_Tech = file_manager.loadFile("Campus/Terre Haute-009917.xlsx")

main_campus = Ivy_Tech.get_building("main")
center_work_development = Ivy_Tech.get_building("center")

Ivy_Tech.display_items()

'''
==========================
BUILDING TEST FUNCTIONS
==========================
'''

# -=Swap building variables out below to test the different buildings=-

#main_campus.display_items()
#main_campus.display_items(science_building.sort_by_name())
#main_campus.display_items(science_building.sort_by_name())

#main_campus.display_items(science_building.sort_by_department())
#main_campus.display_items(science_building.sort_by_department())

#main_campus.display_items(science_building.sort_by_quantity())
#main_campus.display_items(science_building.sort_by_quantity())

#main_campus.display_items(science_building.sort_by_manufacturer())
#main_campus.display_items(science_building.sort_by_manufacturer())

#main_campus.display_items(science_building.sort_by_room())
#main_campus.display_items(science_building.sort_by_room())

# -=Examples of the filters=-
#main_campus.display_items(science_building.filter_by_name("beak"))
#main_campus.display_items(english_building.filter_by_name("note"))
