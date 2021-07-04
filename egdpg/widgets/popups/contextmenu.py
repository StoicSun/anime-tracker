# a popup exist until you click away from it. By default, a right click activates the popup.

import dearpygui.dearpygui as dpg

with dpg.window(label="Tutorial", width=500, height=500):

    dpg.add_text("Right Click Me")

    with dpg.popup(dpg.last_item()):
        dpg.add_text("A popup")
        dpg.add_button(label="Do something")

dpg.start_dearpygui()
