import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Tutorial"):
    dpg.add_text("Right Click Me")

    with dpg.popup(dpg.last_item()):
        dpg.add_text("A popup")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
