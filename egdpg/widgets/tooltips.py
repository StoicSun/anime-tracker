# Tooltips are windows that appear when a widget is hovered.

import dearpygui.dearpygui as dpg

with dpg.window(label="Tutorial"):
    
    tooltip_parent = dpg.add_text("Hover me")
    
    with dpg.tooltip(tooltip_parent): # Have to pass the widget which the tooltip is targeting
        dpg.add_text("A tooltip")

dpg.start_dearpygui()
