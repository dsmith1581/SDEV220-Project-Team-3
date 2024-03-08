# Project Team 3 (Alexander Smith, Daniel Smith, John Sharp)
# Ivy Tech Asset Manager - GUI
# Implements the GUI for the rest of the program.

from file_manager import FileManager
from campus import Campus
from building import Building
from detect_theme import get_os_theme
from equipment import Equipment

import re
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

def assets_to_string(assets):
    asset_string = ""
    for asset in assets:
        # Check if this is not the first line being added
        if asset_string != "":
            # If not, make sure we've moved to a new line
            asset_string += "\n"
        # And then add the next line
        asset_string += asset.get_item_name() + " | " + asset.get_description()
    return numbered_lines(asset_string)

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
    asset_details = assets_to_string(current_building.get_items())

    # Create the widgets to be displayed, starting with the campus info
    campus_label = ttk.Label(root_window, text = campus_name)

    # Building dropdown
    building_selection = tkinter.StringVar(root_window)
    building_selection.set(building_names[0])

    #building_menu = ttk.OptionMenu(root_window, tkinter.StringVar(value=current_building_name()), *building_names)
    building_menu = ttk.OptionMenu(root_window, building_selection, building_selection.get(), *building_names)

    # Spinbox for inventory ID selector
    max_value = len(current_building.get_items())
    if max_value < 1:
            max_value = 1
    inventory_spinbox = ttk.Spinbox(root_window, from_=1, to=max_value, width=5)
    inventory_spinbox.set(1)

    # Inventory buttons
    inventory_label = ttk.Label(root_window, text = "Inventory ID:")
    inventory_add_button = ttk.Button(root_window, text = "Add", command=add_inventory_workflow)
    # The details button needs to call the inventory_details function with arguments
    def inventory_details_helper():
        # Skip when we have no items in an inventory yet
        if len(current_building.get_items()) == 0:
            return
        # Find some info about what the current asset is
        current_index = int(inventory_spinbox.get())
        asset = current_building.get_items()[current_index]
        # Now call the actual inventory details function
        inventory_details(asset)

    inventory_details_button = ttk.Button(root_window, text = "Details", command=inventory_details_helper)
    
    # Asset info output area
    asset_info = tkinter.scrolledtext.ScrolledText(root_window, font=("Courier", 10))
    asset_info.insert(tkinter.END, asset_details)

    # Back button
    def go_back():
        # Clear the window and load the initial view
        clear_window()
        main_view()

        return

    back_button = ttk.Button(root_window, text = "<- Back", command=go_back)


    # Configure grid expandability
    root_window.grid_rowconfigure(3, weight = 1)
    root_window.grid_columnconfigure(2, weight = 1)

    # Place items in grid
    campus_label.grid(            row = 0, column = 0, columnspan = 3, padx = (5, 0), pady = (0, 10), sticky = "w")
    back_button.grid(             row = 0, column = 3, columnspan = 1, padx = (0, 5), pady = (10, 0), sticky = "nw")
    building_menu.grid(           row = 1, column = 0, columnspan = 3, padx = (5, 0), pady = (0, 10), sticky = "w")
    inventory_label.grid(         row = 2, column = 0, columnspan = 1, padx = (5, 0), pady = (0, 10), sticky = "w")
    inventory_spinbox.grid(       row = 2, column = 1, columnspan = 1, padx = (5, 0), pady = (0, 10), sticky = "w")
    inventory_details_button.grid(row = 2, column = 2, columnspan = 1, padx = (5, 0), pady = (0, 10), sticky = "w")
    inventory_add_button.grid(    row = 2, column = 3, columnspan = 1, padx = (5, 0), pady = (0, 10), sticky = "w")
    asset_info.grid(              row = 3, column = 0, columnspan = 4, padx = (5, 5), pady = (0,  5), sticky = "nsew")

    # Handle campus selection changes
    def on_building_selection_change(*args):
        nonlocal current_building_index
        current_building_index = building_names.index(building_selection.get());
        current_building = campus.get_building(current_building_name())
        
        # Update asset info
        asset_details = assets_to_string(current_building.get_items())
        asset_info.delete(1.0, tkinter.END)
        asset_info.insert(tkinter.END, asset_details)

        # Update spinbox range and reset to the default value
        max_value = len(current_building.get_items())
        if max_value < 1:
            max_value = 1

        print(max_value)

        inventory_spinbox.config(from_=1, to=max_value)
        inventory_spinbox.set(1)

        return

    building_selection.trace('w', on_building_selection_change)

# Clears the contents of a window. Useful for switching views
def clear_window():
    for widget in root_window.winfo_children():
        widget.destroy();

    return

# Create the main window
def create_window():
    global root_window
    root_window = tkinter.Tk()
    root_window.title("Ivy Tech Inventory System")

    # Set the theme
    root_window.tk.call("source", "theme/azure.tcl")
    # Dynamically detect the OS theme and set ours appropriately
    root_window.tk.call("set_theme", get_os_theme())
    root_window.iconbitmap("theme/logos/ivy_tech.ico")

    # Set the initial dimensions of the window to something small so it fits on most screens
    root_window.geometry("640x480")

    # Initialize to the main view
    main_view()

    # Run the application
    root_window.mainloop()

    return

# Popup window to see the details of an asset
def inventory_details(asset):
    # Gather the asset details
    details = f"Name: {asset.get_item_name()}\nQuantity in room: {asset.get_room_quantity()}\nDescription: {asset.get_description()}\nDepartment: {asset.get_department()}\nBuilding: {asset.get_from_building()}\nManufacturer: {asset.get_manufacturer()}"
    
    # Show them to the user
    tkinter.messagebox.showinfo(f"{asset.get_item_name()} - Detailed Information", details)

    return

# Creates the initial view where you select which file to open
def main_view():
    # Create an intro message
    message_label = ttk.Label(root_window, text = "Welcome to the Ivy Tech Inventory System")
    message_label.pack(pady = (10, 20))
    # And stick the logo below that
    global logo_image
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

    return

# Handles creating a new inventory
def new_inventory():
    file_path = filedialog.asksaveasfilename(defaultextension = ".xlsx", filetypes = [("Excel Files", "*.xlsx")])

    # If we didn't select a file then don't do anything
    if not file_path:
        tkinter.messagebox.showinfo("Inventory Creation Cancelled", "No new file was selected, cancelling creation of new inventory.")
        return

    # This function will be called when the button is clicked
    buildings_input = tkinter.simpledialog.askstring("Input", """Enter a list of alphanumeric building names e.g. "Main Building,Student Life,Health Professions":""", parent = root_window)

    # Bail if nothing was entered
    if buildings_input == "":
        tkinter.messagebox.showinfo("Inventory Creation Cancelled", "No building names entered, cancelling creation of new inventory.")
        return

    # Bail if incorrect values were entered
    if not re.match(r"""^[a-zA-Z0-9_\-, ]{1,}$""", buildings_input):
        tkinter.messagebox.showinfo("Inventory Creation Cancelled", "Building names had unsupported characters instead of alphanumeric, cancelling creation of new inventory.")
        return

    # Go create the actual Excel sheet now
    file_manager = FileManager()
    file_manager.create_file(file_path, buildings_input.split(","))

    # And launch the gui on it automatically
    load_file(file_path)

    return

# Adds right justified line numbers to a string
def numbered_lines(string):
    # Split the string into lines
    lines = string.split("\n")
    # Get the length of the final number string to know how much to pad the numbers to
    max_width = len(str(len(lines)))
    # Combine all the lines with their number and appropriate number of padding
    result =  "\n".join(f"{str(i+1).rjust(max_width)}.  {line}" for i, line in enumerate(lines))

    return result

# Handles selecting a file and loading the inventory from that
def select_and_load_file():
    file_path = tkinter.filedialog.askopenfilename(
        # Only show .xlsx files
        filetypes = [("Excel files", "*.xlsx")]
    )

    if file_path:
        load_file(file_path)

    return


### Backend related functions
# Load a file
def load_file(file_path):
    file_manager = FileManager()
    campus = file_manager.load_file(file_path)

    # Switch to campus view
    clear_window()
    campus_view(campus)

    return


### Launch the GUI
create_window()
