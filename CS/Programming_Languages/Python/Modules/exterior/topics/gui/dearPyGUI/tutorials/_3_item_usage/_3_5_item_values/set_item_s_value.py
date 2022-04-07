import dearpygui.dearpygui as dpg

dpg.create_context()

def print_value(sender):
    print(dpg.get_value(sender))

with dpg.window(width=300):
    # Creating a slider_int widget and setting the
    # default value to 15.
    dpg.add_slider_int(default_value=15, tag="slider_int", callback=print_value)
    print_value('slider_int')

# On second thought, we're gonna set the value to 40
# instead - for no reason in particular...
dpg.set_value("slider_int", 40)
print_value('slider_int')

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
