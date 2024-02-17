from file_manager import FileManager
from campus import Campus
from building import Building
from equipment import Equipment

file_manager = FileManager()
ivy_tech = file_manager.load_file("Campus/Terre Haute-009917.xlsx")

main_campus = ivy_tech.get_building("main")
center_work_development = ivy_tech.get_building("center")

ivy_tech.display_items()

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
