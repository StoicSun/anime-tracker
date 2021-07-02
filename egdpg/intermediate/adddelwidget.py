import dearpygui.dearpygui as dpg

# pregenerate ids so that they can be passed on to add_button 
# and delete_buttons functions since to add or delete an item u need its uuid
delete_button = dpg.generate_uuid()
secondary_window = dpg.generate_uuid()

# id's will be generated later
new_button1 = 0
new_button2 = 0

def add_buttons():
    global new_button1, new_button2
    new_button1 = dpg.add_button(label="New Button", before=delete_button)
    new_button2 = dpg.add_button(label="New Button 2", parent=secondary_window)

def delete_buttons():
    dpg.delete_item(new_button1)
    dpg.delete_item(new_button2)


with dpg.window(label="Tutorial", pos=(200, 200)):
    dpg.add_button(label="Add Buttons", callback=add_buttons)
    dpg.add_button(label="Delete Buttons", callback=delete_buttons, id=delete_button)

with dpg.window(label="Secondary Window", id=secondary_window, pos=(100, 100)):
    pass

# Only deleting chlidren of a parent container example
window = dpg.generate_uuid()

def delete_children():
    dpg.delete_item(window, children_only=True)

with dpg.window(label="Parent", pos=(200, 200), id=window):
    dpg.add_button(label="Delete Children", callback=delete_children)
    dpg.add_button(label="Button_1")
    dpg.add_button(label="Button_2")
    dpg.add_button(label="Button_3")

dpg.start_dearpygui()
