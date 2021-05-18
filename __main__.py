from character import * # comes with character_armor and character_stats
from items import *

from tkinter import *

root = Tk()
root.geometry("300x300")
root.iconbitmap("icon.ico")
main_frame = Frame(root)
main_frame.pack()

left_frame = Frame(root)
left_frame.pack(side=LEFT)
right_frame = Frame(root)
right_frame.pack(side=RIGHT)
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)




characters_frame = Frame(root)
gear_frame = Frame(root)
weapons_frame = Frame(root)
armor_frame = Frame(root)


# This is bad but inputs don't seem to work for these functions, nor does putting the command in "command = " directly
def characters_page():
    main_frame.pack_forget()
    left_frame.pack_forget()
    right_frame.pack_forget()
    characters_frame.pack()
    label = Label(characters_frame, textvariable = top_text)
    top_text.set("Characters not yet implemented!")

def gear_page():
    main_frame.pack_forget()
    left_frame.pack_forget()
    right_frame.pack_forget()
    gear_frame.pack()
    label = Label(gear_frame, textvariable = top_text)
    top_text.set("Gear not yet implemented!")

def weapons_page():
    main_frame.pack_forget()
    left_frame.pack_forget()
    right_frame.pack_forget()
    weapons_frame.pack()
    label = Label(weapons_frame, textvariable = top_text)
    top_text.set("Weapons not yet implemented!")

def armor_page():
    main_frame.pack_forget()
    left_frame.pack_forget()
    right_frame.pack_forget()
    armor_frame.pack()
    label = Label(armor_frame, textvariable = top_text)
    top_text.set("Armor not yet implemented!")

def characters_back():
    characters_frame.pack_forget()
    main_frame.pack()
    left_frame.pack()
    right_frame.pack()
    
def gear_back():
    gear_frame.pack_forget()
    main_frame.pack()
    left_frame.pack()
    right_frame.pack()

def weapons_back():
    weapons_frame.pack_forget()
    main_frame.pack()
    left_frame.pack()
    right_frame.pack()

def armor_back():
    armor_frame.pack_forget()
    main_frame.pack()
    left_frame.pack()
    right_frame.pack()


top_text = StringVar()
top_text.set("Main Page")
main_label = Label(main_frame, textvariable = top_text)
main_label.pack()

characters_text = StringVar()
characters_text.set("Characters not yet implemented!")
characters_label = Label(characters_frame, textvariable = characters_text)
characters_label.pack()

gear_text = StringVar()
gear_text.set("Gear not yet implemented!")
gear_label = Label(gear_frame, textvariable = gear_text)
gear_label.pack()

weapons_text = StringVar()
weapons_text.set("Weapons not yet implemented!")
weapons_label = Label(weapons_frame, textvariable = weapons_text)
weapons_label.pack()

armor_text = StringVar()
armor_text.set("Characters not yet implemented!")
armor_label = Label(armor_frame, textvariable = armor_text)
armor_label.pack()


character_button = Button(left_frame, text = "Characters", command = characters_page)
character_button.pack(padx = 4, pady = 3)

gear_button = Button(right_frame, text = "Gear", command = gear_page)
gear_button.pack(padx = 5, pady = 5)

weapons_button = Button(right_frame, text = "Weapons", command = weapons_page)
weapons_button.pack(padx = 5, pady = 5)

armor_button = Button(right_frame, text = "Armor", command = armor_page)
armor_button.pack(padx = 10, pady = 5)

c_back = Button(characters_frame, text = "Back to main page", command = characters_back)
c_back.pack(padx = 0, pady = 0)

g_back = Button(gear_frame, text = "Back to main page", command = gear_back)
g_back.pack(padx = 0, pady = 0)

w_back = Button(weapons_frame, text = "Back to main page", command = weapons_back)
w_back.pack(padx = 0, pady = 0)

a_back = Button(armor_frame, text = "Back to main page", command = armor_back)
a_back.pack(padx = 0, pady = 0)


root.title("Cyberpunk 2020 DM Kit")
root.mainloop()