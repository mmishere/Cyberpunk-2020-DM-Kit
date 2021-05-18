from collections import namedtuple
from peewee import *

# note that -1 is used to denote "see notes for cost"

db = SqliteDatabase('items.db')

class Gear(Model):
    name = CharField()
    cost = TextField()
    description = TextField()
    type = CharField()
    notes = TextField()
    class Meta:
        database = db

class Weapon(Model):
    name = CharField()
    cost = FloatField()
    type = CharField() # e.g. melee, pistol
    weapon_accuracy = IntegerField()
    concealability = CharField()
    availability = CharField()
    damage = CharField() # eg. 2D6 + 1
    # the following only  apply to non-melee
    num_shots = IntegerField()
    rate_of_fire = IntegerField()
    # the following apply to both melee and distance
    range = CharField() # str because "throw" is a valid range, not just numbers
    notes = TextField() # extra info, may be empty

    class Meta:
        database = db

BodyParts = namedtuple("BodyParts", "head torso left_arm right_arm left_leg right_leg")
# use True and False to show whether the armor covers a given area

class Armor(Model):
    name = CharField()
    cost = FloatField()
    body_parts = BodyParts # tuple of True/False; see above
    sp = int
    ref_pentalty = int
    notes = str # extra info, may be an empty string; may affect things when printing

    class Meta:
        database = db

db.connect()

# alter_column_type(Gear, cost, cost)


# all of these are already done
# Gear.create_table()
# Weapon.create_table()

# Armor.drop_table()
# Armor.create_table()


# Deleting an item:
# idnumber = 129
# to_delete = Gear.get(Gear.id == idnumber)
# to_delete.delete_instance()

# Updating an item:
# idnumber = 129
# to_update = Gear.get(Gear.id == idnumber)
# to_update.cost = "20.00 / level"
# to_update.notes = "Difficulties: Low Security is AVERAGE (15), Medium Security is DIFFICULT (20), high security is VERY DIFFICULT (25), Maximum Security is NEARLY IMPOSSIBLE (30)."
# five.save()





# for g in Gear.select():
    # print(g.type)
    # if (g.cost == "-1.0"):
    # if (g.notes != ""):
    #     print(str(g.id) + " | " + g.cost + " | " + g.notes)
    # print(g.cost)
    # print(g.name)
    # print(str(g.id) + "\n   " + g.name + "\n   " + g.cost + "\n   " + g.description + "\n   " + g.type + "\n   " + g.notes)
    # print(g.id, g.name)
    # new_item = Gear2TheSequel.create(name=g.name, cost=str(g.cost), description=g.description, type=g.type, notes=g.notes)
    # new_item.save()


# For me to input items with:
# while True:
#     # run through and add in items
#     item_type = input("g, w, a, stop: ")
#     if (item_type == 'g'):
#         x_type = input("type: ")
#         x_name = input("name: ")
#         x_cost = float(input("cost: "))
#         x_descr = input("description: ")
#         x_notes = input("notes: ")
#         # gear = Gear(name=x_name, cost=x_cost, description=x_descr, type=x_type, notes=x_notes)
#         # gear.save()
#         gear = Gear.create(name=x_name, cost=x_cost, description=x_descr, type=x_type, notes=x_notes)
#         gear.save()

#     elif (item_type == 'w'):
#         x_name = input("name: ")
#         x_cost = float(input("cost: "))
#         x_type = input("type: ")
#         x_wa = int(input("WA: "))
#         x_conc = input("conceal: ")
#         x_avail = input("avail: ")
#         x_dmg = input("dmg: ")
#         x_num_shots = int(input("num shots:" ))
#         x_rof = int(input("RoF: "))
#         x_range = input("range: ")
#         x_notes = input("notes: ")
#         weapon = Weapon(name=x_name, cost=x_cost, type=x_type, weapon_accuracy = x_wa, concealability=x_conc, damage=x_dmg, rate_of_fire=x_rof, range=x_range, notes=x_notes )
#         weapon.save()

#     elif (item_type == 'a'):
#         x_name = input("name: ")
#         x_cost = float(input("cost: "))
#         x_penalty = input("ref penalty: ")

#         x_head = bool(input("head: "))
#         x_torso = bool(input("torso: "))
#         x_ra = bool(input("r. arm: "))
#         x_la = bool(input("l. arm: "))
#         x_rl = bool(input("r. leg: "))
#         x_ll = bool(input("l. leg: "))
#         x_parts = BodyParts(x_head, x_torso, x_ra, x_la, x_rl, x_ll)

#         armor = Armor(name=x_name, cost=x_cost, body_parts = x_parts)
#         armor.save()
#     elif (item_type == "stop"):
#         break
#     else:
#         print("Bad input")


def add_gear():
    x_type = input("Any fields can be left empty if desired.\nInput gear type: ")
    x_name = input("Input gear name: ")
    x_cost = float(input("Input gear cost: "))
    x_descr = input("Input gear description: ")
    x_notes = input("Input gear notes (extra information, if applicable): ")
    gear = Gear.create(name=x_name, cost=x_cost, description=x_descr, type=x_type, notes=x_notes)
    gear.save()

def remove_gear(name):
    gear = Gear.get(Gear.name == name)
    gear.delete_instance()

def add_weapon():
    # ADD TYPE CHECKING SO THAT PEOPLE CAN'T INPUT UNDESIRED CHARS, E.G. LETTERS WHERE NUMBERS SHOULD BE
    # except for cases where the cost is a range or something?? or unlisted. hm.
    w_name = input("Any fields can be left empty if desired.\nInput weapon name: ")
    w_cost = float(input("Input weapon cost: "))
    w_type = input("Input weapon type: ")
    w_wa = input("Input weapon WA: ")
    if (w_wa == ""):
        w_wa = 0 # int
    w_conc = input("Input weapon conceal: ")
    w_avail = input("Input weapon avail: ")
    w_dmg = input("Input weapon dmg: ")
    w_num_shots = int(input("Input weapon num shots:" ))
    if (w_num_shots == ""):
        w_num_shots = 0 # int
    w_rof = int(input("Input weapon RoF: "))
    if (w_rof == ""):
        w_rof = 0 # int
    w_range = input("Input weapon range: ")
    w_notes = input("Input weapon notes (extra information, if applicable): ")
    weapon = Weapon(name=w_name, cost=w_cost, type=w_type, weapon_accuracy = w_wa, concealability=w_conc, damage=w_dmg, rate_of_fire=w_rof, range=w_range, notes=w_notes)
    weapon.save()

def remove_weapon(name):
    weapon = Weapon.get(Weapon.name == name)
    weapon.delete_instance()

def add_armor():
    x_name = input("Input armor name: ")
    x_cost = float(input("Input armor cost: "))
    x_penalty = input("Input armor REF penalty: ")

    x_head = bool(input("Input head SP: "))
    x_torso = bool(input("Input torso SP: "))
    x_ra = bool(input("Input right arm SP: "))
    x_la = bool(input("Input left arm SP: "))
    x_rl = bool(input("Input right leg SP: "))
    x_ll = bool(input("Input left leg SP: "))
    x_parts = BodyParts(x_head, x_torso, x_ra, x_la, x_rl, x_ll)

    armor = Armor(name=x_name, cost=x_cost, penalty = x_penalty, body_parts = x_parts)
    armor.save()