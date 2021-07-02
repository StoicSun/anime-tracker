import dearpygui.dearpygui as dpg

def button_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")

with dpg.window(label="Tutorial"):

    name = dpg.add_input_text(label="Your name")
    dpg.add_button(label="Dummy", callback=button_callback, user_data="Some Data")
    dpg.add_button(label="Submit", callback=button_callback, user_data=lambda: dpg.get_value(name))    

dpg.start_dearpygui() 
