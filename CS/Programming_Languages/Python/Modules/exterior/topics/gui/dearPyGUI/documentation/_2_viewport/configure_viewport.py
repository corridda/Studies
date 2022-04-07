import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Example Window", width=500, height=150):
    dpg.add_text("Hello, world")

dpg.create_viewport(title='Custom Title', width=600, height=200)  # create viewport takes in config options too!

# must be called before showing viewport
dpg.set_viewport_small_icon("c:/Program Files/Total Commander/Totalcmd.ico")
dpg.set_viewport_large_icon("c:/Program Files/Total Commander/Totalcmd.ico")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
