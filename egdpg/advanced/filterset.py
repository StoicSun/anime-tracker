# Didn't understand everything but got a general gist
import dearpygui.dearpygui as dpg

# generate ids
filter_id = dpg.generate_uuid()
input_id = dpg.generate_uuid()

def callback(sender):
    
    # get value from input box
    filter_string = dpg.get_value(sender)

    # set value of filter set
    dpg.set_value(filter_id, filter_string)

with dpg.window(label="tutorial"):

    dpg.add_input_text(label="Filter (inc, -exc)", callback=callback)
    # The filter set app item is a container that can be used to filter its children based on their filter_key.
    with dpg.filter_set(id=filter_id):
        dpg.add_text("aaa1.c", filter_key="aaa1.c", bullet=True)
        dpg.add_text("bbb1.c", filter_key="bbb1.c", bullet=True)
        dpg.add_text("ccc1.c", filter_key="ccc1.c", bullet=True)
        dpg.add_text("aaa2.cpp", filter_key="aaa2.cpp", bullet=True)
        dpg.add_text("bbb2.cpp", filter_key="bbb2.cpp", bullet=True)
        dpg.add_text("ccc2.cpp", filter_key="ccc2.cpp", bullet=True)
        dpg.add_text("abc.h", filter_key="abc.h", bullet=True)
        dpg.add_text("hello, world", filter_key="hello, world", bullet=True)

dpg.start_dearpygui()
