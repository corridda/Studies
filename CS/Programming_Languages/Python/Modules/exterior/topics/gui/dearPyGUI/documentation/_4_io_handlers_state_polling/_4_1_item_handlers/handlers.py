import dearpygui.dearpygui as dpg

dpg.create_context()


def change_text(sender, app_data):
    dpg.set_value(app_data[1], f"Mouse Button ID: {app_data}")


def visible_call(sender, app_data):
    print("I'm visible")


with dpg.item_handler_registry(tag="widget handler") as handler:
    dpg.add_item_clicked_handler(callback=change_text)
    dpg.add_item_visible_handler(callback=visible_call)

with dpg.window(width=500, height=300):
    text_1 = dpg.add_text("Click me with any mouse button", tag="text item")
    text_2 = dpg.add_text("Close window with arrow to change visible state printing to console", tag="text item 2")

# bind item handler registry to item
dpg.bind_item_handler_registry(text_1, "widget handler")
dpg.bind_item_handler_registry(text_2, "widget handler")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
