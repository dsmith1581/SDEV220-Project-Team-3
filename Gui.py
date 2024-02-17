from file_manager import FileManager
from campus import Campus
from building import Building
from equipment import Equipment

import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk



### GUI related functions
# Creates a modal view for defining a new inventory item
def add_inventory_workflow():
    # TODO - implement inventory workflow modal
    alert_unimplemented()

def alert_unimplemented():
    tkinter.messagebox.showinfo("Unimplemented Function", "This functionality is not yet implemented!")

# Creates a view which contains the controls and outputs for a particular loaded campus
def campus_view(campus):
    # Use the campus location as the display name
    campus_name = campus.get_location()

    # Get a list of the buildings to select from and assume the default building is the first in the list
    building_names = [building.get_building_name() for building in campus.get_buildings()]
    current_building_index = 0
    def current_building_name():
        return building_names[current_building_index]
    current_building = campus.get_building(current_building_name())

    # Load the assets for that building
    assets = current_building.get_items()
    asset_details = ""
    for asset in assets:
        asset_details += asset.get_item_name() + "\n"


    # Create the widgets to be displayed, starting with the campus info
    campus_label = ttk.Label(root_window, text = campus_name)

    # Building dropdown
    building_selection = tkinter.StringVar(root_window)
    building_selection.set(building_names[0])
    building_menu = ttk.OptionMenu(root_window, tkinter.StringVar(value=current_building_name()), *building_names)

    # Inventory add/remove buttons
    inventory_label = ttk.Label(root_window, text = "Inventory:")
    inventory_add_button = ttk.Button(root_window, text = "Add", command=add_inventory_workflow)
    inventory_remove_button = ttk.Button(root_window, text = "Remove", command=remove_inventory_workflow)

    # Asset info output area
    asset_info = tkinter.scrolledtext.ScrolledText(root_window, font=("Courier", 10))
    asset_info.insert(tkinter.END, asset_details)
    

    # Configure grid expandability
    root_window.grid_rowconfigure(3, weight = 1)
    root_window.grid_columnconfigure(2, weight = 1)

    # Place items in grid
    campus_label.grid(           row = 0, column = 0, columnspan = 3, padx = (5, 0), pady = (0, 10), sticky = "w")
    building_menu.grid(          row = 1, column = 0, columnspan = 3, padx = (5, 0), pady = (0, 10), sticky = "w")
    inventory_label.grid(        row = 2, column = 0, columnspan = 1, padx = (5, 0), pady = (0, 10), sticky = "w")
    inventory_add_button.grid(   row = 2, column = 1, columnspan = 1, padx = (5, 0), pady = (0, 10), sticky = "w")
    inventory_remove_button.grid(row = 2, column = 2, columnspan = 1, padx = (5, 0), pady = (0, 10), sticky = "w")
    asset_info.grid(             row = 3, column = 0, columnspan = 3, padx = (5, 5), pady = (0,  5), sticky = "nsew")


# Clears the contents of a window. Useful for switching views
def clear_window():
    for widget in root_window.winfo_children():
        widget.destroy();

# Create the main window
def create_window():
    global root_window
    root_window = tkinter.Tk()
    root_window.title("Ivy Tech Inventory System")

    # Set the theme
    root_window.tk.call("source", "theme/azure.tcl")
    root_window.tk.call("set_theme", "light")
    root_window.iconbitmap("theme/logos/ivy_tech.ico")

    # Set the initial dimensions of the window to something small so it fits on most screens
    root_window.geometry("640x480")

    # Create an intro message
    message_label = ttk.Label(root_window, text = "Welcome to the Ivy Tech Inventory System")
    message_label.pack(pady = (10, 20))
    # And stick the logo below that
    logo_image = tkinter.PhotoImage(file = "theme/logos/ivy_tech_full.ppm")
    logo_label = tkinter.Label(root_window, image = logo_image)
    logo_label.pack(pady = (0, 50))

    # Create some buttons to start with
    # Open an existing file
    open_file_button = ttk.Button(root_window, text = "Select File to Load", command = select_and_load_file)
    open_file_button.pack(pady = 20, padx = 20)
    # Create a new file
    new_file_button = ttk.Button(root_window, text = "New Inventory", command = new_inventory)
    new_file_button.pack(pady = 20, padx = 20)

    # Run the application
    root_window.mainloop()

# Handles creating a new inventory
def new_inventory():
    # TODO - implement new inventory creation process
    alert_unimplemented();

# Popup window workflow to delete an inventory item
def remove_inventory_workflow():
    # TODO - implement inventory workflow modal
    alert_unimplemented()

# Handles selecting a file and loading the inventory from that
def select_and_load_file():
    file_path = tkinter.filedialog.askopenfilename(
        # Only show .xlsx files
        filetypes = [("Excel files", "*.xlsx")]
    )

    if file_path:
        load_file(file_path)



### Backend related functions
# Load a file
def load_file(file_path):
    file_manager = FileManager()
    campus = file_manager.load_file(file_path)

    # Switch to campus view
    clear_window()
    campus_view(campus)



# Launch the GUI
create_window()
