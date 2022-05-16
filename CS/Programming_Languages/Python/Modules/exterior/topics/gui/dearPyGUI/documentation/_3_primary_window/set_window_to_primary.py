import dearpygui.dearpygui as dpg

dpg.create_context()

def press_me_callback(sender, appdata):
    with dpg.window(
        label='window 2',
        pos=[200, 200],
    ) as window_2:
        dpg.add_text("Inside window 2")

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")

with dpg.window(
    label='window 1',
    pos=[200,0],
    modal=True
) as window_1:
    dpg.add_text("Inside window 1")
    dpg.add_button(
        label="Press me!",
        callback=press_me_callback
    )

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
