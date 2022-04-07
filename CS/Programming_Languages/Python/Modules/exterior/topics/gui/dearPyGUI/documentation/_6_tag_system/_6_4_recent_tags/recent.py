import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Example") as wnd_1:
    with dpg.group() as grp_1:
        bttn_1 = dpg.add_button(label="View the Terminal for item tags")
        print(f"bttn_1: {bttn_1}")
        print(f"dpg.last_item(): {dpg.last_item()}")
        print(f"grp_1: {grp_1}")
        print(f"dpg.last_container(): {dpg.last_container()}")
        print(f"wnd_1: {wnd_1}")
        print(f"dpg.last_root(): {dpg.last_root()}")

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
