from Campus import Campus
from Building import Building
from Equipment import Equipment

Ivy_Tech = Campus("Terre Haute", "009917")
Ivy_Tech.set_buildings(
    [
        Building("Science Hall"),
        Building("English Hall"),
        Building("Tech Hall")
    ]
)

science_building = Ivy_Tech.get_building("science")
english_building = Ivy_Tech.get_building("english")
tech_building = Ivy_Tech.get_building("tech")

science_building.set_items([
    Equipment(
        "Beaker",
        room_quantity= {"B101": 5, "B102":3, "P203":10},
        department=["BIO", "PHYS"],
        manufacturer="Glass Company",
        description="A glass beaker."
    ),
    Equipment(
        "Hot Tables",
        room_quantity= {"P203":10},
        department=["PHYS"],
        manufacturer="Dell",
        description="These get hot watch out."
    ),
    Equipment(
        "Computer",
        room_quantity= {"B101": 8, "B102":8},
        department=["BIO"],
        manufacturer="Dell",
        description="Dell computers, a bunch of them."
    ),
])
english_building.set_items([
    Equipment(
        "English Books",
        room_quantity= {"E101": 5, "E102":3},
        department=["ENG"],
        manufacturer="Textbook Company",
        description="Textbooks..."
    ),
    Equipment(
        "Notebooks",
        room_quantity= {"E203":10},
        department=["ENG"],
        manufacturer="Paper Dudes",
        description="Bro I can draw in these while the professor talks."
    ),
])

# Below are test functions, uncomment and run to see how they work.
# Sort functions toggle order between ascending and descending if
# used muiltiple times in a row.
'''
==========================
CAMPUS-WIDE TEST FUNCTIONS
==========================
'''
#Ivy_Tech.display_items()
#Ivy_Tech.display_items(Ivy_Tech.sort_by_name())
#Ivy_Tech.display_items(Ivy_Tech.sort_by_name())

#Ivy_Tech.display_items(Ivy_Tech.sort_by_department())
#Ivy_Tech.display_items(Ivy_Tech.sort_by_department())

#Ivy_Tech.display_items(Ivy_Tech.sort_by_quantity())
#Ivy_Tech.display_items(Ivy_Tech.sort_by_quantity())

#Ivy_Tech.display_items(Ivy_Tech.sort_by_manufacturer())
#Ivy_Tech.display_items(Ivy_Tech.sort_by_manufacturer())

#Ivy_Tech.display_items(Ivy_Tech.sort_by_room())
#Ivy_Tech.display_items(Ivy_Tech.sort_by_room())

# -=Examples of the filters=-
#Ivy_Tech.display_items(Ivy_Tech.filter_by_name("beak"))
#Ivy_Tech.display_items(Ivy_Tech.filter_by_department("PHYS"))

'''
==========================
BUILDING TEST FUNCTIONS
==========================
'''
# -=Swap building variables out below to test the different buildings=-

#science_building.display_items()
#science_building.display_items(science_building.sort_by_name())
#science_building.display_items(science_building.sort_by_name())

#science_building.display_items(science_building.sort_by_department())
#science_building.display_items(science_building.sort_by_department())

#science_building.display_items(science_building.sort_by_quantity())
#science_building.display_items(science_building.sort_by_quantity())

#science_building.display_items(science_building.sort_by_manufacturer())
#science_building.display_items(science_building.sort_by_manufacturer())

#science_building.display_items(science_building.sort_by_room())
#science_building.display_items(science_building.sort_by_room())

# -=Examples of the filters=-
#science_building.display_items(science_building.filter_by_name("beak"))
#english_building.display_items(english_building.filter_by_name("note"))
