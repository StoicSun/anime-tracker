import dearpygui.dearpygui as dpg

with dpg.window(label="stretched",pos=[0,0]):

    with dpg.table(header_row=False, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                borders_outerH=True, borders_innerV=True, borders_outerV=True):

        dpg.add_table_column(label="Header 1")
        dpg.add_table_column(label="Header 2")
        dpg.add_table_column(label="Header 3")

        for i in range(0, 5):
            for j in range(0, 3):
                dpg.add_text(f"Row{i} Column{j}")
                if not (i == 4 and j == 2):
                    dpg.add_table_next_column()

with dpg.window(label="fixed", pos=[500,100], width=400, height=200):

    # Only available if scrollX/scrollY are disabled and stretch columns are not used
    with dpg.table(header_row=False, policy=dpg.mvTable_SizingFixedFit, resizable=True, no_host_extendX=True, 
                borders_innerV=True, borders_outerV=True, borders_outerH=True):

        dpg.add_table_column(label="Header 1")
        dpg.add_table_column(label="Header 2")
        dpg.add_table_column(label="Header 3")

        for i in range(0, 5):
            for j in range(0, 3):
                dpg.add_text(f"Row{i} Column{j}")
                if not (i == 4 and j == 2):
                    dpg.add_table_next_column()

with dpg.window(label="mixed", pos=[500,400], width=600, height=200):

    with dpg.table(header_row=True, policy=dpg.mvTable_SizingFixedFit, row_background=True, reorderable=True, 
                resizable=True, no_host_extendX=False, hideable=True, 
                borders_innerV=True, delay_search=True, borders_outerV=True, borders_innerH=True, borders_outerH=True):

        dpg.add_table_column(label="AAA", width_fixed=True)
        dpg.add_table_column(label="BBB", width_fixed=True)
        dpg.add_table_column(label="CCC", width_stretch=True, init_width_or_weight=0.0)
        dpg.add_table_column(label="DDD", width_stretch=True, init_width_or_weight=0.0)

        for i in range(0, 5):
            for j in range(0, 4):
                if j == 2 or j == 3:
                    dpg.add_text(f"Stretch {i},{j}")
                else:
                    dpg.add_text(f"Fixed {i}, {j}")
                if not (i == 4 and j == 3):
                    dpg.add_table_next_column()

dpg.start_dearpygui()