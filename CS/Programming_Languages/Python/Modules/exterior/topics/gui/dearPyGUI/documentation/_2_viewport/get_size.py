import ctypes
import dearpygui.dearpygui as dpg

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(f"screensize: {screensize}")
print(f"type(screensize): {type(screensize)}")


dpg.create_context()


def delete_children():
    dpg.delete_item("window", children_only=True)


with dpg.window(label="Tutorial", pos=(200, 200), tag="window"):
    dpg.add_button(label="Delete Children", callback=delete_children)
    dpg.add_button(label="Button_1")
    dpg.add_button(label="Button_2")
    dpg.add_button(label="Button_3")

dpg.create_viewport(
    title='Custom Title',
    width=screensize[0],
    height=screensize[1],
    x_pos=0,
    y_pos=0,
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()