import dearpygui.dearpygui as dpg

# To add your own fonts, you must first create a font registry to add fonts to. 
with dpg.font_registry():
    
    # adding font to registry (set as default for entire app)
    dpg.add_font("egdpg/intermediate/font/Inter-Regular.ttf", 20, default_font=True)

    # add second font
    secondary_font = dpg.add_font("egdpg/intermediate/font/Retron2000.ttf", 13)

with dpg.window(label="Font Example") as pw:
    dpg.add_button(label="Default font")
    dpg.add_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin eu nibh eu erat tristique varius quis id justo. Donec at facilisis urna, eu consequat felis. Sed a nisi pulvinar, varius est vitae, porta felis. Praesent ut enim sit amet ex facilisis gravida sed eu massa. Fusce id tellus nec sapien auctor efficitur at quis lectus. Cras a ante ut turpis scelerisque iaculis. Nullam at dui tellus. Proin fringilla est quis neque viverra, eget hendrerit diam placerat. In volutpat placerat dolor, ac sodales odio. ", 
    wrap=300)
    secbtn = dpg.add_button(label="Secondary font")
    
    # set font of specific widget
    dpg.set_item_font(secbtn, secondary_font)

dpg.set_primary_window(pw, True)

dpg.start_dearpygui()

# Note: Diff languages font can be added by increasing their range of characters
# using range hints see https://github.com/hoffstadt/DearPyGui/wiki/Fonts#loading-specific-unicode-characters