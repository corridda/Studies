import dearpygui.dearpygui as dpg

dpg.create_context()


def stage_items():
    with dpg.stage(tag="stage1"):
        for i in range(5):
            dpg.add_text(f"({i}): hello, i was added from a stage")


def present_stage_items():
    dpg.push_container_stack("main_win")
    dpg.unstage("stage1")
    dpg.pop_container_stack()


with dpg.window(label="Tutorial", tag="main_win", height=400, width=400):
    dpg.add_button(label="stage items", callback=stage_items)
    dpg.add_button(label="present stages items", callback=present_stage_items)

dpg.show_item_registry()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
