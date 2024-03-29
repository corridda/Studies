import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.theme() as disabled_theme:
    with dpg.theme_component(dpg.mvInputFloat, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 150])

    with dpg.theme_component(dpg.mvInputInt, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 150])

dpg.bind_theme(disabled_theme)

with dpg.window(label="tutorial"):
    dpg.add_input_float(label="Input float", enabled=True)
    dpg.add_input_float(label="Input float", enabled=False)
    dpg.add_input_int(label="Input int", enabled=False)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
