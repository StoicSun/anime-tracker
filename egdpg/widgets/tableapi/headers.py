import dearpygui.dearpygui as dpg

with dpg.window(label="tutorial"):

    with dpg.table(header_row=True):

        # use add_table_column to add columns to the table,
        # table columns use slot 0
        dpg.add_table_column(label="Header 1")
        dpg.add_table_column(label="Header 2")
        dpg.add_table_column(label="Header 3")

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, 4):
            for j in range(0, 3):
                dpg.add_text(f"Row{i} Column{j}")
                if not (i == 3 and j == 2):
                    dpg.add_table_next_column()

dpg.start_dearpygui()

