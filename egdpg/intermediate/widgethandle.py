import dearpygui.dearpygui as dpg

def change_text(sender, app_data):
    handler = sender
    # Getting the widget to which the handler is binded to
    text_item = dpg.get_item_parent(handler)  
    dpg.set_value(text_item, "I was clicked!")

with dpg.window(width=500, height=300):
    text_widget = dpg.add_text("Click me with any mouse button")
    dpg.add_clicked_handler(text_widget, callback=change_text, user_data=text_widget)

dpg.start_dearpygui()