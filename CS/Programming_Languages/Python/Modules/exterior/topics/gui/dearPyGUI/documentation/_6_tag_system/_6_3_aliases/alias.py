import dearpygui.dearpygui as dpg

dpg.create_context()


def callback():
    print(dpg.get_value("unique_tag"))


with dpg.window(label="Example"):
    dpg.add_button(label="Press me (print to output)", callback=callback)
    dpg.add_input_int(default_value=5, label="Input", tag="unique_tag")

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
