import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Tutorial"):
    b0 = dpg.add_button(label="button 0")
    b1 = dpg.add_button(tag=100, label="Button 1")
    b2 = dpg.add_button(tag="Btn2", label="Button 2")

print(f"b0: {b0}")
print(f"b1: {b1}")
print(f"b2: {b2}")
print(f"dpg.get_item_label('Btn2'): {dpg.get_item_label('Btn2')}")

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()