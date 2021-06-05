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
        self.top_label.grid(row = 0, column = 50) # column isn't quite centering properly

        self.handle = Entry(self, **options_bw, width = 15, font = (courier_new, 14), justify = 'center')
        self.handle.insert(0, "Enter Handle")
        self.handle.grid(row = 1, column = 0, padx = 20)
        self.role = Entry(self, **options_bw, width = 15, font = (courier_new, 14), justify = 'center')
        self.role.insert(0, "Enter Role")
        self.role.grid(row = 2, column = 0)

        # used for is_npc
        self.is_npc = IntVar(self, value=False)
        self.chara = Radiobutton(self, **options_bw, text = "Player", font = (courier_new, 14), variable = self.is_npc, value = False, selectcolor = 'black', anchor = 'w')
        self.chara.grid(row = 3, column = 0)
        self.npc = Radiobutton(self, **options_bw, text = "NPC", font = (courier_new, 14), variable = self.is_npc, value = True, selectcolor = 'black', anchor = 'w')
        self.npc.grid(row = 4, column = 0)

        # set stats
        self.INT_val = IntVar(self, value = 0)
        self.REF_val = IntVar(self, value = 0)
        self.TECH_val = IntVar(self, value = 0)
        self.COOL_val = IntVar(self, value = 0)
        self.ATTR_val = IntVar(self, value = 0)
        self.LUCK_val = IntVar(self, value = 0)
        self.MA_val = IntVar(self, value = 0)
        self.BODY_val = IntVar(self, value = 0)
        self.EMP_val = IntVar(self, value = 0)

        INT_label = Label(self, text = "INT", **options_bw, font = (courier_new, 14))
        REF_label = Label(self, text = "REF", **options_bw, font = (courier_new, 14))
        TECH_label = Label(self, text = "TECH", **options_bw, font = (courier_new, 14))
        COOL_label = Label(self, text = "COOL", **options_bw, font = (courier_new, 14))
        ATTR_label = Label(self, text = "ATTR", **options_bw, font = (courier_new, 14))
        LUCK_label = Label(self, text = "LUCK", **options_bw, font = (courier_new, 14))
        MA_label = Label(self, text = "MA", **options_bw, font = (courier_new, 14))
        BODY_label = Label(self, text = "BODY", **options_bw, font = (courier_new, 14))
        EMP_label = Label(self, text = "EMP", **options_bw, font = (courier_new, 14))

        INT_input = Entry(self, textvariable = self.INT_val, width = 2, **options_bw, font = (courier_new, 14))
        REF_input = Entry(self, textvariable = self.REF_val, width = 2, **options_bw, font = (courier_new, 14))
        TECH_input = Entry(self, textvariable = self.TECH_val, width = 2, **options_bw, font = (courier_new, 14))
        COOL_input = Entry(self, textvariable = self.COOL_val, width = 2, **options_bw, font = (courier_new, 14))
        ATTR_input = Entry(self, textvariable = self.ATTR_val, width = 2, **options_bw, font = (courier_new, 14))
        LUCK_input = Entry(self, textvariable = self.LUCK_val, width = 2, **options_bw, font = (courier_new, 14))
        MA_input = Entry(self, textvariable = self.MA_val, width = 2, **options_bw, font = (courier_new, 14))
        BODY_input = Entry(self, textvariable = self.BODY_val, width = 2, **options_bw, font = (courier_new, 14))
        EMP_input = Entry(self, textvariable = self.EMP_val, width = 2, **options_bw, font = (courier_new, 14))

        INT_label.grid(row = 10, column = 0)
        INT_input.grid(row = 10, column = 1)

        REF_label.grid(row = 11, column = 0)
        REF_input.grid(row = 11, column = 1)

        TECH_label.grid(row = 12, column = 0)
        TECH_input.grid(row = 12, column = 1)

        COOL_label.grid(row = 13, column = 0)
        COOL_input.grid(row = 13, column = 1)

        ATTR_label.grid(row = 14, column = 0)
        ATTR_input.grid(row = 14, column = 1)

        LUCK_label.grid(row = 15, column = 0)
        LUCK_input.grid(row = 15, column = 1)

        MA_label.grid(row = 16, column = 0)
        MA_input.grid(row = 16, column = 1)

        BODY_label.grid(row = 17, column = 0)
        BODY_input.grid(row = 17, column = 1)

        EMP_label.grid(row = 18, column = 0)
        EMP_input.grid(row = 18, column = 1)


        self.eb = DoubleVar(self, value = 0.0)
        self.description = StringVar(self, value = "")
        self.notes = StringVar(self, value = "")
        # eb
        # description
        # notes
        # armor

        self.enter_character = Button(self, **options_bw, text = "Create character", font = (courier_new, 12), command = lambda: self.create_character())
        self.enter_character.grid(row = 30, column = 30)



    def create_character(self):
        print("creating character")

        int_ = self.INT_val.get()
        ref_ = self.REF_val.get()
        tech_ = self.TECH_val.get()
        cool_ = self.COOL_val.get()
        attr_ = self.ATTR_val.get()
        luck_ = self.LUCK_val.get()
        ma_ = self.MA_val.get()
        body_ = self.BODY_val.get()
        emp_ = self.EMP_val.get()

        stats_ = Stats(int_, ref_, tech_, cool_, attr_, luck_, ma_, body_, emp_)
        stats_serialized = serialize_stats(stats_)
        # hp isn't set intentionally, it should just be 40 in all cases for 2020 characters
        # TODO: set cyberware, gear, armor
        new_character = Character(handle=self.handle.get(), role=self.role.get(), is_npc=self.is_npc.get(), eb=self.eb.get(), description=self.description.get(), notes=self.notes.get(), stats=stats_serialized)
        add_character(new_character)
        print("Handle: " + new_character.handle + ", Role: " + new_character.role + ", NPC: " + str(new_character.is_npc))


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cyberpunk 2020 DM Kit")
        self.geometry('900x600')
        self.configure(bg = 'black')
        self.iconbitmap('icon.ico')

        self.frames = {}
        for fr in (MainFrame, NewCharacterFrame):
            frame = fr(self)
            self.frames[fr] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew") # packing is done here
        
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

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()