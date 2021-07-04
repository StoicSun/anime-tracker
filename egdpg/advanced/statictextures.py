# Static textures are used for images that do not change often. They are typically loaded at startup. If they need to be updated, you would delete and recreate them. 
# These accept python lists, tuples, numpy arrays

import dearpygui.dearpygui as dpg

texture_data = []
for i in range(0, 100*100):
    texture_data.append(255/255)
    texture_data.append(0)
    texture_data.append(255/255)
    texture_data.append(255/255)

with dpg.texture_registry():
    texture_id = dpg.add_static_texture(100, 100, texture_data)

with dpg.window(label="Tutorial"):
    dpg.add_image(texture_id)

dpg.start_dearpygui()
