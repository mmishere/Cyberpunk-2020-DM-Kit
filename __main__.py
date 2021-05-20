from character import * # comes with character_armor and character_stats
from items import *
from menu_functions import *

from tkinter import *


default_font = 'Courier New'
root = Tk()
root.geometry("900x600")
root.configure(bg = 'black')
root.iconbitmap("icon.ico")
main_frame = Frame(root)
main_frame.pack()

top_text = StringVar()
top_text.set("Main Page")
main_label = Label(main_frame, textvariable = top_text)
main_label.configure(bg = 'black', fg = 'red', font = (default_font, 16))
main_label.pack()

# Setting the background and foreground here will only work for Linux users - I'm not entirely sure if it will, as I don't have Linux.
menu_bar = Menu(main_frame, bg = 'black', fg = 'white')
menu_bar.add_command(label = "Main Page", command = main_tab)

character_menu = Menu(menu_bar, tearoff = 0)
character_menu.add_command(label = "All", command = all_characters)
character_menu.add_command(label = "Players", command = players)
character_menu.add_command(label = "NPCs", command = npcs)
menu_bar.add_cascade(label = "Characters", menu = character_menu)

gear_menu = Menu(menu_bar, tearoff = 0)
gear_menu.add_command(label = "All", command = all_gear)
gear_menu.add_command(label = "Fashion", command = fashion)
gear_menu.add_command(label = "Personal Electronics", command = personal_electronics)
gear_menu.add_command(label = "Data Systems", command = data_systems)
gear_menu.add_command(label = "Communications", command = communications)
gear_menu.add_command(label = "Surveillance", command = surveillance)
gear_menu.add_command(label = "Entertainment", command = entertainment)
gear_menu.add_command(label = "Security", command = security)
gear_menu.add_command(label = "Medical", command = medical)
gear_menu.add_command(label = "Furnishings", command = furnishings)
gear_menu.add_command(label = "Vehicles", command = vehicles)
gear_menu.add_command(label = "Lifestyle", command = lifestyle)
gear_menu.add_command(label = "Groceries", command = groceries)
gear_menu.add_command(label = "Housing", command = housing)
gear_menu.add_command(label = "Miscellaneous", command = miscellaneous_gear)
# misc is for player-added items with no type
menu_bar.add_cascade(label = "Gear", menu = gear_menu)


weapons_menu = Menu(menu_bar, tearoff = 0)
weapons_menu.add_command(label = "All", command = all_weapons)
weapons_menu.add_command(label = "Pistols", command = pistols)
weapons_menu.add_command(label = "SMGs", command = smgs)
weapons_menu.add_command(label = "Shotguns", command = shotguns)
weapons_menu.add_command(label = "Rifles", command = rifles)
weapons_menu.add_command(label = "Heavy Weapons", command = heavy_weapons)
weapons_menu.add_command(label = "Melee", command = melee)
weapons_menu.add_command(label = "Exotic", command = exotic)
weapons_menu.add_command(label = "Miscellaneous", command = miscellaneous_weapons)
# misc is for player-added items with no type
menu_bar.add_cascade(label = "Weapons", menu = weapons_menu)

armor_menu = Menu(menu_bar, tearoff = 0)
armor_menu.add_command(label = "All", command = all_armor)
menu_bar.add_cascade(label = "Armor", menu = armor_menu)


options_menu = Menu(menu_bar, tearoff = 0)
options_menu.add_command(label = "Full Screen", command = full_screen)
options_menu.add_command(label = "Windowed", command = windowed)
options_menu.add_command(label = "Light Mode", command = light_mode)
options_menu.add_command(label = "Dark Mode", command = dark_mode)
# misc is for player-added items with no type
menu_bar.add_cascade(label = "Options", menu = options_menu)
# options: full screen, windowed, light mode, dark mode

root.config(menu = menu_bar)

root.title("Cyberpunk 2020 DM Kit")
root.mainloop()