"""Usage

https://console-menu.readthedocs.io/en/latest/usage.html
"""

import consolemenu
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem, CommandItem
from consolemenu import SelectionMenu


menu = ConsoleMenu("This is a menu!", "It has a subtitle too!")

command_item = CommandItem("Run a console command", "touch hello.txt")
function_item = FunctionItem("Call a function", input, ["Enter some input"])

submenu = ConsoleMenu("This is the submenu")
submenu_item = SubmenuItem("Show a submenu", submenu, menu=menu)

menu.append_item(command_item)
menu.append_item(function_item)
menu.append_item(submenu_item)
menu.show()

# a_list = ["red", "blue", "green"]
# selection = SelectionMenu.get_selection(a_list)
# print(selection)