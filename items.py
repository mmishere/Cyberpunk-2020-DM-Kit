from collections import namedtuple
from peewee import *

# note that -1 is used to denote "see notes for cost"

db = SqliteDatabase('items.db')

class Gear(Model):
    name = CharField()
    cost = FloatField()
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
    notes = str # extra info, may be an empty string; may affect things when printing

    class Meta:
        database = db

db.connect()
# all of these are already done
# Gear.create_table()
# Weapon.create_table()
# Armor.create_table()

# how we delete items from the db:
# idnumber = 111
# grandma = Gear.get(Gear.id == idnumber)
# grandma.delete_instance()

for g in Gear.select():
    # print(str(g.id) + "\n   " + g.name + "\n   " + str(g.cost) + "\n   " + g.description + "\n   " + g.type + "\n   " + g.notes)
    print(g.id, g.name)
# make sure to check all types afterwards for consistency


# print(Gear.select().where(Gear.name == 'Kibble').get())
while True:
    # run through and add in items
    item_type = input("g, w, a, stop: ")
    if (item_type == 'g'):
        x_type = input("type: ")
        x_name = input("name: ")
        x_cost = float(input("cost: "))
        x_descr = input("description: ")
        x_notes = input("notes: ")
        # gear = Gear(name=x_name, cost=x_cost, description=x_descr, type=x_type, notes=x_notes)
        # gear.save()
        gear = Gear.create(name=x_name, cost=x_cost, description=x_descr, type=x_type, notes=x_notes)
        gear.save()

    elif (item_type == 'w'):
        x_name = input("name: ")
        x_cost = float(input("cost: "))
        x_type = input("type: ")
        x_wa = int(input("WA: "))
        x_conc = input("conceal: ")
        x_avail = input("avail: ")
        x_dmg = input("dmg: ")
        x_num_shots = int(input("num shots:" ))
        x_rof = int(input("RoF: "))
        x_range = input("range: ")
        x_notes = input("notes: ")
        weapon = Weapon(name=x_name, cost=x_cost, type=x_type, weapon_accuracy = x_wa, concealability=x_conc, damage=x_dmg, rate_of_fire=x_rof, range=x_range, notes=x_notes )
        weapon.save()

    elif (item_type == 'a'):
        x_name = input("name: ")
        x_cost = float(input("cost: "))

        x_head = bool(input("head: "))
        x_torso = bool(input("torso: "))
        x_ra = bool(input("r. arm: "))
        x_la = bool(input("l. arm: "))
        x_rl = bool(input("r. leg: "))
        x_ll = bool(input("l. leg: "))
        x_parts = BodyParts(x_head, x_torso, x_ra, x_la, x_rl, x_ll)

        armor = Armor(name=x_name, cost=x_cost, body_parts = x_parts)
        armor.save()
    elif (item_type == "stop"):
        break
    else:
        print("Bad input")


# def add_gear(gear):
#     gear.save()

# def remove_gear(gear):
#     gear.delete_instance()

# def add_weapon(weapon):
#     weapon.save()

# def remove_weapon(weapon):
#     weapon.delete_instance()
