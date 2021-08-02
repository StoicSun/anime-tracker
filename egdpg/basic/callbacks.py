from dearpygui import dearpygui as dpg

def button_callback(sender, app_data, user_data):

	text_input = dpg.get_value(user_data)
	print(f"sender is: {sender}")
	print(f"app_data is: {app_data}")
	print(f"user_data is: {user_data}")
	print(f"text_input is: {text_input}")

with dpg.window(label="Tutorial"):

	name = dpg.add_input_text(label="Your name")
	dpg.add_button(label="Submit", callback=button_callback, user_data=name)

dpg.start_dearpygui()
