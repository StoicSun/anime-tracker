import dearpygui.dearpygui as dpg

with dpg.window(label="tutorial"):

    with dpg.table(header_row=False, row_background=True,
                            borders_innerH=True, borders_outerH=True, borders_innerV=True,
                            borders_outerV=True):

        # use add_table_column to add columns to the table,
        # table columns use slot 0
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, 4):
            for j in range(0, 3):
                dpg.add_text(f"Row{i} Column{j}")
                if not (i == 3 and j == 2):
                    dpg.add_table_next_column()

dpg.start_dearpygui()