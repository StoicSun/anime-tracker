# A theme is composed of theme colors and styles
# The theme can either be set as the default theme, attached to an app item type, a item container, or a specific item.
# in simpler words themes can be specific to an widget or can be globally set to all items

# 4 ways of applying themes

# 1. Apply theme to specific item
import dearpygui.dearpygui as dpg

with dpg.window(label="Specific"):
    button1 = dpg.add_button(label="Button 1")
    button2 = dpg.add_button(label="Button 2")

# create a theme
with dpg.theme() as theme_id:
    dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 140, 23), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

dpg.set_item_theme(button1, theme_id) # Applying theme only to button1

dpg.start_dearpygui()