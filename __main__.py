from character import * # comes with character_armor and character_stats
from items import *

from tkinter import *


print("imports are compiling")


root = Tk()
root.geometry("300x300")
frame = Frame(root)
frame.pack()

left_frame = Frame(root)
left_frame.pack(side=LEFT)
right_frame = Frame(root)
right_frame.pack(side=RIGHT)
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)


# This is bad but inputs don't seem to work for these functions, nor does putting the command in "command = " directly
def character_not_yet():
    top_text.set("Characters not yet implemented!")

def gear_not_yet():
    top_text.set("Gear not yet implemented!")

def weapons_not_yet():
    top_text.set("Weapons not yet implemented!")

def armor_not_yet():
    top_text.set("Armor not yet implemented!")


top_text = StringVar()
top_text.set("")

label = Label(frame, textvariable = top_text)
label.pack()

character_button = Button(frame, text = "Characters", command = character_not_yet)
character_button.pack(padx = 4, pady = 3)

gear_button = Button(left_frame, text = "Gear", command = gear_not_yet)
gear_button.pack(padx = 5, pady = 5)

weapons_button = Button(left_frame, text = "Weapons", command = weapons_not_yet)
weapons_button.pack(padx = 5, pady = 5)

armor_button = Button(right_frame, text = "Armor", command = armor_not_yet)
armor_button.pack(padx = 10, pady = 5)


root.title("Cyberpunk 2020 Ref Kit")
root.mainloop()

# glowstick = Gear(name="Glowstick", cost=5.50, description="Exactly what you think it is.", type="Utility", notes="")
# print(glowstick.name, glowstick.description)