from character import * # comes with character_armor and character_stats
from items import *
from menu_placeholders import * # remove this later once all frames are set up

from tkinter import *

courier_new = 'Courier New'

options_br = {'bg': 'black', 'fg': 'red'} # black red
options_bw = {'bg': 'black', 'fg': 'white'} # black white

class MainFrame(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.configure(bg = 'black')
        self.label = Label(self, **options_br, text = 'Main Menu', font = (courier_new, 16))
        self.label.pack(padx = 10, pady = 5)

class NewCharacterFrame(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.configure(bg = 'black')

        self.top_label = Label(self, text = "New Character")
        self.top_label.configure(**options_br, font = (courier_new, 16))
        self.top_label.pack()

        self.handle = Entry(self, **options_bw, width = 0, font = (courier_new, 12))
        self.handle.insert(0, 'Enter Handle')
        self.handle.pack()
        self.role = Entry(self, **options_bw, width = 0, font = (courier_new, 12))
        self.role.insert(0, 'Enter Role')
        self.role.pack()

        self.npc_str = IntVar(self, value=True)
        self.chara = Radiobutton(self, **options_bw, text = "Player character", font = (courier_new, 12), variable = self.npc_str, value = False)
        self.chara.pack()
        self.npc = Radiobutton(self, **options_bw, text = "NPC", font = (courier_new, 12), variable = self.npc_str, value = True)
        self.npc.pack()

        self.enter_character = Button(self, **options_bw, text = "Create character", font = (courier_new, 12), command = lambda: self.create_character)
        self.enter_character.pack()

    def create_character():
        h = handle.get()
        n = npc_str.get()
        r = role.get()
        print(h, n, r)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Cyberpunk 2020 DM Kit')
        self.geometry('900x600')
        self.configure(bg = 'black')
        self.iconbitmap('icon.ico')

        self.frames = {}
        for fr in (MainFrame, NewCharacterFrame):
            # commented out string-based frames:
            # frame_name = fr.__name__
            # frame = fr(container, self)
            # self.frames[frame_name] = frame
            # frame.pack()
            frame = fr(self)
            self.frames[fr] = frame
            frame.pack()
            # frame.grid(row = 0, column = 0, sticky = "nsew") # packing is done here
        
        self.show_frame(MainFrame)


        self.menu_bar = Menu(self)
        
        # i tried to abstract this bit into a function and it didn't work, so :')
        self.menu_bar.add_command(label = "Main Menu", command = lambda: self.show_frame(MainFrame))
        character_menu = Menu(self.menu_bar, tearoff = 0)
        character_menu.add_command(label = "All", command = lambda: self.show_frame(AllCharactersFrame))
        character_menu.add_command(label = "New Character", command = lambda: self.show_frame(NewCharacterFrame))
        character_menu.add_command(label = "NPCs", command = lambda: self.show_frame(NPCsFrame))
        character_menu.add_command(label = "Players", command = lambda: self.show_frame(PlayersFrame))

        self.menu_bar.add_cascade(label = "Characters", menu = character_menu)

        gear_menu = Menu(self.menu_bar, tearoff = 0)
        gear_menu.add_command(label = "All", command = lambda: self.show_frame(AllGearFrame))
        gear_menu.add_command(label = "Communications", command = lambda: self.show_frame(CommunicationsFrame))
        gear_menu.add_command(label = "Data Systems", command = lambda: self.show_frame(DataSystemsFrame))
        gear_menu.add_command(label = "Entertainment", command = lambda: self.show_frame(EntertainmentFrame))
        gear_menu.add_command(label = "Fashion", command = lambda: self.show_frame(FashionFrame))
        gear_menu.add_command(label = "Furnishings", command = lambda: self.show_frame(FurnishingsFrame))
        gear_menu.add_command(label = "Groceries", command = lambda: self.show_frame(GroceriesFrame))
        gear_menu.add_command(label = "Housing", command = lambda: self.show_frame(HousingFrame))
        gear_menu.add_command(label = "Lifestyle", command = lambda: self.show_frame(LifestyleFrame))
        gear_menu.add_command(label = "Medical", command = lambda: self.show_frame(MedicalFrame))
        gear_menu.add_command(label = "Miscellaneous", command = lambda: self.show_frame(MiscGearFrame)) # for player-added items with no type
        gear_menu.add_command(label = "Personal Electronics", command = lambda: self.show_frame(PersonalElectronicsFrame))
        gear_menu.add_command(label = "Security", command = lambda: self.show_frame(SecurityFrame))
        gear_menu.add_command(label = "Surveillance", command = lambda: self.show_frame(SurveillanceFrame))
        gear_menu.add_command(label = "Vehicles", command = lambda: self.show_frame(VehiclesFrame))
        self.menu_bar.add_cascade(label = "Gear", menu = gear_menu)


        weapons_menu = Menu(self.menu_bar, tearoff = 0)
        weapons_menu.add_command(label = "All", command = lambda: self.show_frame(AllWeaponsFrame))
        weapons_menu.add_command(label = "Exotics", command = lambda: self.show_frame(ExoticsFrame))
        weapons_menu.add_command(label = "Heavy Weapons", command = lambda: self.show_frame(HeavyWeaponsFrame))
        weapons_menu.add_command(label = "Melee", command = lambda: self.show_frame(MeleeFrame))
        weapons_menu.add_command(label = "Miscellaneous", command = lambda: self.show_frame(MiscWeaponsFrame))  # for player-added items with no type
        weapons_menu.add_command(label = "Pistols", command = lambda: self.show_frame(PistolsFrame))
        weapons_menu.add_command(label = "Rifles", command = lambda: self.show_frame(RiflesFrame))
        weapons_menu.add_command(label = "Shotguns", command = lambda: self.show_frame(ShotgunsFrame))
        weapons_menu.add_command(label = "SMGs", command = lambda: self.show_frame(SMGsFrame))


        # misc is for player-added items with no type
        self.menu_bar.add_cascade(label = "Weapons", menu = weapons_menu)

        armor_menu = Menu(self.menu_bar, tearoff = 0)
        armor_menu.add_command(label = "All", command = lambda: self.show_frame(AllArmorFrame))
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
        try:
            print("showing frame: " + to_show.__name__)
            frame = self.frames[to_show]
            frame.tkraise()
        except:
            print(to_show)

if __name__ == '__main__':
    app = App()
    frame = MainFrame(app)
    app.mainloop()