# Apply theme to a container

import dearpygui.dearpygui as dpg

with dpg.window(label="tutorial") as window_id:
    button1 = dpg.add_button(label="Button 1")
    button2 = dpg.add_button(label="Button 2")

with dpg.window(label="dumdum") as window_id2: # Theme will not be applied to this window
    button1 = dpg.add_button(label="Button 1")
    button2 = dpg.add_button(label="Button 2")

# create a theme
with dpg.theme() as theme_id:
    dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 140, 23), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

dpg.set_item_theme(window_id, theme_id) # Applying theme to the whole window

dpg.start_dearpygui()
