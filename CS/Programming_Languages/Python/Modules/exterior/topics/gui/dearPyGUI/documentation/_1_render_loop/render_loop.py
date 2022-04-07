import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")

dpg.show_viewport()

cntr = 1

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    print(f"cntr: {cntr}")
    dpg.render_dearpygui_frame()
    cntr += 1

    if cntr > 200:
        dpg.stop_dearpygui()

dpg.destroy_context()
