import dearpygui.dearpygui as dpg

#  You have to unpack the properties of the image from the loader
# Paths are relative to the main directory it seems
width, height, channels, data = dpg.load_image('egdpg\\intermediate\\mushi.jpg') # 0: width, 1: height, 2: channels, 3: data

with dpg.texture_registry():
    image_id = dpg.add_static_texture(width, height, data)

with dpg.window(label="Tutorial"):

    with dpg.drawlist(width=700, height=700):

        dpg.draw_image(image_id, (0, 400), (200, 600), uv_min=(0, 0), uv_max=(1, 1))
        dpg.draw_image(image_id, (400, 300), (600, 500), uv_min=(0, 0), uv_max=(0.5, 0.5))
        dpg.draw_image(image_id, (0, 0), (300, 300), uv_min=(0, 0), uv_max=(2.5, 2.5))

dpg.start_dearpygui()
