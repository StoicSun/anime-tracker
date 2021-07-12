import dearpygui.dearpygui as dpg
from usrdb import usrdb 

animes = [row for row in usrdb.returnrows()]


# Dummy function
def print_me(sender):
    print(f"Menu Item: {sender}")


# Function to add new anime to db
def addtodb(sender, app_data, user_data):
    usrdb.addrow(user_data)
    # Close the connection when done writing to db
    usrdb.con.close()


with dpg.font_registry():
    dpg.add_font("amnesiac/font/OpenSans-Regular.ttf", 20, default_font=True)
    secondary_font = dpg.add_font("amnesiac/font/Gomme Sans W04 Regular.ttf", 19)

# Primary window
with dpg.window(label="Amnesia V-0.1.0") as pw:
    # Menu bar
    with dpg.menu_bar() as mb:

        with dpg.menu(label="File"):

            dpg.add_menu_item(label="Import Database", callback=print_me)
            dpg.add_menu_item(label="Export Database", callback=print_me)

        with dpg.menu(label="Settings"):

            with dpg.menu(label="Theme"):
                dpg.add_menu_item(label="Dark")
                dpg.add_menu_item(label="Light")

            dpg.add_menu_item(label="Setting 2", callback=print_me)

        with dpg.menu(label="Help"):

            dpg.add_menu_item(label="Getting started", callback=print_me)
            dpg.add_menu_item(label="Check for updates...")
            dpg.add_menu_item(label="About")

    dpg.set_item_font(mb, secondary_font)

    # Input row
    aname = dpg.add_input_text(hint="Anime's name", label='', width=300)
    dpg.add_same_line()
    adate = dpg.add_date_picker(label="Date", default_value={
                                'month day': 2, 'year': 20, 'month': 1}, show=False)
    dpg.add_same_line()
    submitbtn = dpg.add_button(label=" Add ")
    dpg.add_clicked_handler(submitbtn, callback=addtodb,
                            user_data=lambda: dpg.get_value(aname))

    # Data table
    with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                   row_background=True, borders_innerV=True, borders_outerV=True, borders_innerH=True, borders_outerH=True):
        dpg.add_table_column(label="Id", width_fixed=True)
        dpg.add_table_column(
            label="Name", width_stretch=True, init_width_or_weight=0.0)
        dpg.add_table_column(label="Ep", width_stretch=True,
                             init_width_or_weight=0.2, default_sort=True)
        dpg.add_table_column(label="State", width_fixed=True)
        dpg.add_table_column(label="Date", width_fixed=True)
        for row in animes:
            dpg.add_text(row[0])
            dpg.add_table_next_column()
            dpg.add_text(row[1])
            dpg.add_table_next_column()
            dpg.add_input_int(label='', max_value=999999, show=False) # Hidding the ep input box before click
            dpg.add_text(row[2])
            dpg.add_table_next_column()
            if row[3] == 0:
                dpg.add_text("Watching")
            elif row[3] == 1:
                dpg.add_text("Completed")
            else:
                dpg.add_text("Rewatching")          
            dpg.add_table_next_column()
            dpg.add_text(row[4])
            dpg.add_table_next_column()        


with dpg.theme() as theme_id:
    dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg,
                        (115, 79, 154), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Button, (73, 80,
                        87), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,
                        (255, 107, 107), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,
                        (230, 100, 42), category=dpg.mvThemeCat_Core)
    # dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg,
    #                    (240, 62, 62), category=dpg.mvThemeCat_Core)
    # dpg.add_theme_color(dpg.mvThemeCol_TableRowBg,
    #                    (33, 37, 41), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10,
                        5, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,
                        10, category=dpg.mvThemeCat_Core)

with dpg.theme() as sbtn:
    dpg.add_theme_color(dpg.mvThemeCol_Button, (250, 82,
                        82), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,
                        (255, 107, 107), category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,
                        (255, 120, 108), category=dpg.mvThemeCat_Core)

dpg.set_item_theme(submitbtn, sbtn)

dpg.set_item_theme(pw, theme_id)

dpg.set_primary_window(pw, True)

dpg.start_dearpygui()
