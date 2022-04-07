import dearpygui.dearpygui as dpg

dpg.create_context()


def item_callback(sender, app_data):
    print(f"{dpg.get_value(sender)}")


with dpg.window(label="Tutorial"):
    chb_1 = dpg.add_checkbox(label="Radio Button1", tag="R1", callback=item_callback)
    chb_2 = dpg.add_checkbox(label="Radio Button2", source="R1", callback=item_callback)

    dpg.add_input_text(label="Text Input 1", callback=item_callback)
    dpg.add_input_text(
        label="Text Input 2",
        source=dpg.last_item(),
        password=True,
        callback=item_callback
    )

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
