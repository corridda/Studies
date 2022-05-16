import ctypes

import dearpygui.dearpygui as dpg

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

dpg.create_context()

with dpg.window(label="Example Window", width=500, height=150):
    dpg.add_text("Hello, world")

# dpg.create_viewport(title='Custom Title', width=600, height=200)  # create viewport takes in config options too!
dpg.create_viewport(
    title='Custom Title',
    width=screensize[0],
    height=screensize[1],
    x_pos=0,
    y_pos=0,
    max_width=screensize[0],
    max_height=screensize[1]
)  # create viewport takes in config options too!

# must be called before showing viewport
dpg.set_viewport_small_icon("c:/Program Files/Total Commander/Totalcmd.ico")
dpg.set_viewport_large_icon("c:/Program Files/Total Commander/Totalcmd.ico")

dpg.show_item_registry()

dpg.setup_dearpygui()
dpg.show_viewport(maximized=True)
dpg.start_dearpygui()
dpg.destroy_context()
