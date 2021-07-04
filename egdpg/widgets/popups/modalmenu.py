# When the modal keyword is set to True, the popup will be modal. 
# This prevents the user from interacting with other windows until the popup is closed. 
# To close the popup, you must hide it.

import dearpygui.dearpygui as dpg

with dpg.window(label="Tutorial"):

    dpg.add_text("Left Click Me")

    # First create the popup with modal = True and as modal_id
    # Then set show = False when 'Close' button is clicked
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True) as modal_id:
        dpg.add_button(label="Close", callback=lambda: dpg.configure_item(modal_id, show=False))

dpg.start_dearpygui()
