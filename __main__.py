from character import * # comes with character_armor and character_stats
from items import *
from menu_functions import *

from tkinter import *

# will probably remove this later
import menu_functions


courier_new = 'Courier New'

options_br = {'bg': 'black', 'fg': 'red'} # black red
options_bw = {'bg': 'black', 'fg': 'white'} # black white
options_bb = {'bg': 'black', 'fg': 'black'} # black black

class MainFrame(Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        self.configure(bg = 'black')
        self.label = Label(self, **options_br, text = 'Main Page', font = (courier_new, 16))
        self.label.pack(padx = 10, pady = 5)

class NewCharacterFrame(Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        self.top_label = Label(self, text = "New Character")
        self.top_label.configure(**options_br, font = (courier_new, 16))
        self.top_label.pack()

        self.handle = Entry(self, **options_bw, width = 0, font = (courier_new, 12))
        self.handle.insert(0, 'Enter Handle')
        self.handle.pack()
        self.role = Entry(self, **options_bw, width = 0, font = (courier_new, 12))
        self.role.insert(0, 'Enter Role')
        self.role.pack()
        self.npc_str = IntVar(value=True)
        self.chara = Radiobutton(self, **options_bb, text = "Player character", font = (courier_new, 12), variable = self.npc_str, value = False)
        self.chara.pack()
        self.npc = Radiobutton(self, **options_bb, text = "NPC", font = (courier_new, 12), variable = self.npc_str, value = True)
        self.npc.pack()
        self.enter_character = Button(self, **options_bw, text = "Create character", font = (courier_new, 12), command = self.create_character)
        self.enter_character.pack()

    def create_character():
        h = handle.get()
        n = npc_str.get()
        r = role.get()
        print(h, n, r)

class Frame2(Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller
        self.configure(bg = 'black')
        self.label = Label(self, **options_br, text = 'Test', font = (courier_new, 16))
        self.label.pack(padx = 10, pady = 5)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Cyberpunk 2020 DM Kit')
        self.geometry('900x600')
        self.configure(bg = 'black')
        self.iconbitmap('icon.ico')

        container = Frame(self)
        self.frames = {}
        for fr in (MainFrame, NewCharacterFrame, Frame2):
            frame_name = fr.__name__
            frame = fr(container, self)
            self.frames[frame_name] = frame
            frame.pack()
            # frame.grid(row = 0, column = 0, sticky = "nsew") # packing is done here
        
        self.show_frame("MainFrame")

        # Setting the background and foreground here will only work for Linux users - I'm not entirely sure if it will, as I don't have Linux.
        self.menu_bar = Menu(self, **options_bw)

        # i tried to abstract this bit into a function and it didn't work, so :')
        self.menu_bar.add_command(label = "Main Page", command = lambda: self.show_frame("MainFrame"))
        character_menu = Menu(self.menu_bar, tearoff = 0)
        character_menu.add_command(label = "All", command = all_characters)
        character_menu.add_command(label = "New Character", command = lambda: self.show_frame("NewCharacterFrame"))
        character_menu.add_command(label = "NPCs", command = npcs)
        character_menu.add_command(label = "Players", command = players)

        self.menu_bar.add_cascade(label = "Characters", menu = character_menu)

        gear_menu = Menu(self.menu_bar, tearoff = 0)
        gear_menu.add_command(label = "All", command = all_gear)
        gear_menu.add_command(label = "Communications", command = communications)
        gear_menu.add_command(label = "Data Systems", command = data_systems)
        gear_menu.add_command(label = "Entertainment", command = entertainment)
        gear_menu.add_command(label = "Fashion", command = fashion)
        gear_menu.add_command(label = "Furnishings", command = furnishings)
        gear_menu.add_command(label = "Groceries", command = groceries)
        gear_menu.add_command(label = "Housing", command = housing)
        gear_menu.add_command(label = "Lifestyle", command = lifestyle)
        gear_menu.add_command(label = "Medical", command = medical)
        gear_menu.add_command(label = "Miscellaneous", command = miscellaneous_gear)
        gear_menu.add_command(label = "Personal Electronics", command = personal_electronics)
        gear_menu.add_command(label = "Security", command = security)
        gear_menu.add_command(label = "Surveillance", command = surveillance)
        gear_menu.add_command(label = "Vehicles", command = vehicles)
        # misc is for player-added items with no type
        self.menu_bar.add_cascade(label = "Gear", menu = gear_menu)


        weapons_menu = Menu(self.menu_bar, tearoff = 0)
        weapons_menu.add_command(label = "All", command = all_weapons)
        weapons_menu.add_command(label = "Exotic", command = exotic)
        weapons_menu.add_command(label = "Heavy Weapons", command = heavy_weapons)
        weapons_menu.add_command(label = "Melee", command = melee)
        weapons_menu.add_command(label = "Miscellaneous", command = miscellaneous_weapons)
        weapons_menu.add_command(label = "Pistols", command = pistols)
        weapons_menu.add_command(label = "Rifles", command = rifles)
        weapons_menu.add_command(label = "Shotguns", command = shotguns)
        weapons_menu.add_command(label = "SMGs", command = smgs)


        # misc is for player-added items with no type
        self.menu_bar.add_cascade(label = "Weapons", menu = weapons_menu)

        armor_menu = Menu(self.menu_bar, tearoff = 0)
        armor_menu.add_command(label = "All", command = all_armor)
        self.menu_bar.add_cascade(label = "Armor", menu = armor_menu)


        options_menu = Menu(self.menu_bar, tearoff = 0)
        options_menu.add_command(label = "Full Screen", command = full_screen)
        options_menu.add_command(label = "Windowed", command = windowed)
        options_menu.add_command(label = "Light Mode", command = light_mode)
        options_menu.add_command(label = "Dark Mode", command = dark_mode)
        # misc is for player-added items with no type 
        self.menu_bar.add_cascade(label = "Options", menu = options_menu)
        # options: full screen, windowed, light mode, dark mode

        self.configure(menu = self.menu_bar)
    
    def show_frame(self, to_show):
        print("showing frame")
        frame = self.frames[to_show]
        frame.tkraise()

# if __name__ == '__main__':
app = App()
frame = MainFrame(Frame(app), app)
app.mainloop()