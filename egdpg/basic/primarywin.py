import dearpygui.dearpygui as dpg

with dpg.window(label='Primary window') as pw:
    dpg.add_button(label='dummy')
    dpg.add_checkbox(label='check me pls')
    dpg.add_slider_int(label='slide me pls', default_value=69)
    dpg.add_date_picker(label='pick me pls')

dpg.set_primary_window(pw, True)

dpg.start_dearpygui()