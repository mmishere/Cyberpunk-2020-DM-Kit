from collections import namedtuple
from peewee import *

# note that -1 is used to denote "see notes for cost"

db = SqliteDatabase('info.db')

class Gear(Model):
    name = CharField()
    cost = TextField()
    description = TextField()
    # CHANGED FROM TYPE
    category = CharField()
    notes = TextField()
    class Meta:
        database = db

class Weapon(Model):
    name = CharField()
    cost = TextField()
    # CHANGED FROM TYPE
    category = CharField() # e.g. melee, pistol
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

class Cyberware(Model):
    name = CharField()
    cost = TextField()
    category = CharField()
    description = TextField()
    body_part = CharField()

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

def add_gear():
    x_type = input("Any fields can be left empty if desired.\nInput gear type: ")
    x_name = input("Input gear name: ")
    x_cost = float(input("Input gear cost: "))
    x_descr = input("Input gear description: ")
    x_notes = input("Input gear notes (extra information, if applicable): ")
    gear = Gear.create(name=x_name, cost=x_cost, description=x_descr, type=x_type, notes=x_notes)
    gear.save()

def remove_gear(name: str):
    gear = Gear.get(Gear.name == name)
    gear.delete_instance()


# lets user add their own weapon
# through tk, they select type, etc. and it gets added
# this needs a lot of changes
def add_weapon(name, cost, type_, wa, conc, avail, dmg, num_shots, rof, range, notes):
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

def remove_weapon(name: str):
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