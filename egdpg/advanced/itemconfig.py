import dearpygui.dearpygui as dpg

with dpg.window(label="PPPP"):
    item = dpg.add_button(enabled=True, label="Press me")

# at a later time, change the item's configuration
dpg.configure_item(item, enabled=False, label="New Label")

# All possible item config flags can be seen by doing the following
print(dpg.get_item_configuration(item))

dpg.start_dearpygui()