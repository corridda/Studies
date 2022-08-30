import dearpygui.dearpygui as dpg

dpg.create_context()

def input_int_callback(sender, app_data):
    dpg.set_value("int_value", dpg.get_value(sender))
    print(f"int value: {dpg.get_value('int_value')}")
    print(f"type(int_value): {type(dpg.get_value('int_value'))}")

with dpg.value_registry():
    dpg.add_bool_value(default_value=True, tag="bool_value")
    dpg.add_string_value(default_value="Default string", tag="string_value")
    dpg.add_int_value(tag="int_value")

with dpg.window(label="Tutorial"):
    dpg.add_checkbox(label="Radio Button1", source="bool_value")
    dpg.add_checkbox(label="Radio Button2", source="bool_value")

    dpg.add_input_text(label="Text Input 1", source="string_value")
    dpg.add_input_text(label="Text Input 2", source="string_value", password=True)

    dpg.add_input_int(
        label="Int value",
        callback= input_int_callback,
        on_enter=True
    )


dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
