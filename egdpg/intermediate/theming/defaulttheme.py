import dearpygui.dearpygui as dpg

# create a theme and set it as default
with dpg.theme(default_theme=True) as theme_id:
    dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 140, 23), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

with dpg.window(label="tutorial"):
    button1 = dpg.add_button(label="Button 1")
    button2 = dpg.add_button(label="Button 2")

dpg.start_dearpygui()
