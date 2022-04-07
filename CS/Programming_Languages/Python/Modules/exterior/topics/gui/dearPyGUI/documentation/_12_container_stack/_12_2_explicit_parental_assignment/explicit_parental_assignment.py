import dearpygui.dearpygui as dpg

dpg.create_context()

dpg.add_window(label="Tutorial", tag="window")

dpg.add_menu_bar(parent="window", tag="menu_bar")

dpg.add_menu(label="Themes", parent="menu_bar", tag="themes")
dpg.add_menu_item(label="Dark", parent="themes")
dpg.add_menu_item(label="Light", parent="themes")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
