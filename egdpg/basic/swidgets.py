import dearpygui.dearpygui as dpg

# Creating a context manager with window (container item)
with dpg.window(label="Simple Window"):
    
    
    dpg.add_button(label="Click me")
    
    # Adds next item to the same line as the one before it
    dpg.add_same_line(spacing=10)
    dpg.add_button(label="Click me too")

    # Adds space b/w widgets
    dpg.add_spacing(count=5)

    # printing the widgets unique id
    id=dpg.add_button(label="Press me")
    print(id)

with dpg.window(label="Second Window"):
    dpg.add_slider_int(label="", default_value=0)
    dpg.add_input_text(label="", default_value="lorem ipsum")
    # Playing with checkbox
    cb = dpg.add_checkbox(label="Checkbox")
    # Access value of cb with get_value method
    print("Value before: ",dpg.get_value(cb))
    
    # Set new value with set_value
    dpg.set_value(cb, True)
    print("Value now: ", dpg.get_value(cb))

dpg.start_dearpygui()  # Every dpg script must conclude with this      