import dearpygui.dearpygui as dpg

# This creates a registry(list of known) global handlers
dpg.setup_registries()

def change_text(sender, app_data, user_data):
    # We *pole the item to see its hover state
    if (dpg.is_item_hovered(user_data)): 
        dpg.set_value(user_data, "Stop Hovering Me, Go away!!")
    else:
        dpg.set_value(user_data, "Hover Me!")
with dpg.window(width=500, height=300):
    text_widget = dpg.add_text("Hover Me!")
    dpg.add_mouse_move_handler(callback=change_text, user_data=text_widget)

dpg.start_dearpygui()

# Polling: is the act of checking the devices connected to a 
# parent machine's state 