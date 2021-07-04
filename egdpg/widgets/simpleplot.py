# Simple plots take in a list and plot y-axis data against the number of items in the list. 
# These can be line graphs or histograms and are demonstrated below:

import dearpygui.dearpygui as dpg

with dpg.window(label="Tutorial", width=500, height=500):
    dpg.add_simple_plot(label="Simpleplot1", default_value=(0.3, 0.9, 0.5, 0.3), height=300)
    dpg.add_simple_plot(label="Simpleplot2", default_value=(0.3, 0.9, 2.5, 8.9), overlay="Overlaying", height=180, histogram=True)

dpg.start_dearpygui()
