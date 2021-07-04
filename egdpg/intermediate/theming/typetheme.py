# 2. Apply theme to a type
import dearpygui.dearpygui as dpg

with dpg.window(label="Types") as window_id:
    button1 = dpg.add_button(label="Button 1")
    button2 = dpg.add_button(label="Button 2")

# create a theme
with dpg.theme() as theme_id:
    dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 140, 23), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

dpg.set_item_type_theme(dpg.mvButton, theme_id) # Applying theme to all widgets with button type
dpg.start_dearpygui()