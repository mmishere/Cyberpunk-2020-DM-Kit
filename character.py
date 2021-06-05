from character_stats import *
from character_armor import *
from items import *    

IntrinsicArmor = namedtuple("IntrinsicArmor", "head torso left_arm right_arm left_leg right_leg")
# use True and False to show whether the armor covers a given area
# or numbers? idk

# we have the "db" object here
# for now, role is a string; possibly change to a class of its own later, although custom roles may be problematic
# also need to track lifepath, inventory, descriptions, affectations, etc.
class Character(Model):
    handle = CharField()
    role = CharField()
    is_npc = BooleanField()
    eb = IntegerField(default = 0)
    description = TextField()
    notes = TextField()
    hp = IntegerField(default = 40)
    cyberware = TextField(default = "Not yet implemented") # change later
    gear = TextField(default = "Not yet implemented") # change later
    armor = TextField(default = "Not yet implemented") # change later; ideally we'll have armor as a dict or something filled with Armor objects
    stats = TextField() # serialized Stats object

    class Meta:
        database = db

# Character.drop_table()
# Character.create_table()

def stats_to_string(character: Character):
    # deserialize the stats:
    stats_ = deserialize_stats(character.stats)
    # this looks a bit off if there are any two-digit stat values
    print("STATS for " + character.handle + ":")
    print("  INT  [" + str(stats_.INT) + "]  REF [" + str(stats_.REF) + "] TECH [" + str(stats_.TECH) + "] COOL [" + str(stats_.COOL) + "]")
    print("  ATTR [" + str(stats_.ATTR) + "] LUCK [" + str(stats_.LUCK) + "]   MA [" + str(stats_.MA) + "] BODY [" + str(stats_.BODY) + "]")
    print("  EMP  [" + str(stats_.EMP) + "] Humanity [" + str(stats_.humanity) + "]")
    print("  Run  [" + str(stats_.run) + "m] Leap [" + str(stats_.leap) + "m]")
    print("  Lift [" + str(stats_.lift) + "kgs] Carry [" + str(stats_.carry) + "kgs]")
    # print("  Lift [" + str(int(stats_.lift * 2.20462)) + "lbs] Carry [" + str(int(stats_.carry * 2.20462)) + "]")
    print("  SAVE [" + str(stats_.SAVE) + "] BTM [" + str(stats_.BTM) + "] Melee Modifier [" + str(stats_.melee_modifier) + "], " + stats_.body_type_str)

print("PRINTING ALL CHARACTERS:")
for g in Character.select():
    print(g.handle, g.role, str(g.is_npc), str(g.eb), g.description, g.notes, str(g.hp), g.cyberware, g.gear, g.armor)
    stats_to_string(g)


def add_character(character: Character):
    character.save()


    # can use this for logic when adding characters to db 
        # if stat_values:
        #     self.stats = stat_values
        # else:
        #     self.stats = Character_Stats(0, 0, 0, 0, 0, 0, 0, 0, 0)

# find a more sensible way to do this
# def set_armor(self): # only useful if you want the person to have default armor, e.g. skinweave; won't be used directly by players
#     h = int(input("Input head: "))
#     t = int(input("Input torso: "))
#     ra = int(input("Input right arm: "))
#     la = int(input("Input left arm: "))
#     rl = int(input("Input right leg: "))
#     ll = int(input("Input left leg: "))
#     self.armor.set_armor_values(h, t, ra, la, rl, ll)

    
def set_stats(character: Character):
    INT = int(input("Input INT: "))
    REF = int(input("Input REF: "))
    TECH = int(input("Input TECH: "))
    COOL = int(input("Input COOL: "))
    ATTR = int(input("Input ATTR: "))
    LUCK = int(input("Input LUCK: "))
    MA = int(input("Input MA: "))
    BODY = int(input("Input BODY: "))
    EMP = int(input("Input EMP: "))

    stats_ = Stats(INT, REF, TECH, COOL, ATTR, LUCK, MA, BODY, EMP)
    character.stats = serialize_stats(stats_)
    # character.stats.set_stat_values(INT, REF, TECH, COOL, ATTR, LUCK, MA, BODY, EMP)

def armor_to_string(character: Character):
    pass

def damage(character: Character, damage_amt: int, body_location: str, is_armor_piercing: bool):
    assert body_location == "head" or body_location == "torso" or body_location == "r_arm" or body_location == "l_arm" or body_location == "r_leg" or body_location == "l_leg"
    relevant_armor = character.armor[body_location]
    effective_sp = character.intrinsic_armor[body_location]

    if (relevant_armor != None):
        effective_sp += relevant_armor.sp
        # i think i might be wrong on the rules for stacking armor; check on that
    
    if (is_armor_piercing):
        effective_sp /= 2 # it's okay if effective_sp is 0 here
    
    if (body_location == "head"):
        damage_amt *= 2
    
    if (damage_amt <= effective_sp):
        print("No damage taken!")
        return
    
    damage_amt -= effective_sp
    if (is_armor_piercing):
        damage_amt /= 2
    
    stats_ = deserialize_stats(character.stats)
    damage_amt -= stats_.BTM

    # damage got through, so the armor takes a hit as well
    if (relevant_armor != None):
        character.armor[body_location].sp -= 1

    if (damage_amt <= 0):
        damage_amt = 1
    
    if (damage_amt >= 8):
        print("Effective damage was greater than 8, lost a body part!")
    
    character.hp -= damage_amt

    if (character.hp < 0):
        character.hp = 0
    
    print("Current HP: " + str(character.hp))
    # show character.hp in an easily viewable interface that updates when damage is taken
    # alter armor sp if damage gets through, look into the rules for that

# sample_stats = Character_Stats(10, 10, 5, 3, 5, 6, 9, 4, 6)
# sample_stats_json = serialize_stats(sample_stats)
# bait = Character("Bait", 0, None, None, None, None, None, None, None, None, sample_stats_json)
# stats_to_string(bait)
# damage(bait, 45, "head", False)