from character_stats import *
from character_armor import *
from items import BodyParts, Armor, Gear, Weapon

# also need to track lifepath, inventory, descriptions, affectations, etc.
class Character:
    # add types to cyberware and gear once that's figured out
    def __init__(self, name: str, eb: float, head_armor: Armor, torso_armor: Armor, r_arm_armor: Armor, l_arm_armor: Armor, r_leg_armor: Armor, l_leg_armor: Armor, cyberware, gear, stat_values: Character_Stats):
        self.name = name
        self.eb = eb
        self.cyberware = cyberware
        self.gear = gear
        self.hp = 40

        # setting these now so i don't forget them later; relevant if cyberware increases SP, like Skinweave
        self.intrinsic_armor = {
            "head": 0,
            "torso": 0,
            "r_arm": 0,
            "l_arm": 0,
            "r_leg": 0,
            "l_leg": 0
        }
        
        if stat_values:
            self.stats = stat_values
        else:
            self.stats = Character_Stats(0, 0, 0, 0, 0, 0, 0, 0, 0)
        
        # what if someone has more than one piece of armor on a given part? could make that a list i guess, i dunno
        self.armor = {
            "head": head_armor,
            "torso": torso_armor,
            "r_arm": r_arm_armor,
            "l_arm": l_arm_armor,
            "r_leg": r_leg_armor,
            "l_leg": l_leg_armor
        }
    
    # find a better way to do this
    # def set_armor(self): # only useful if you want the person to have default armor, e.g. skinweave; won't be used directly by players
    #     h = int(input("Input head: "))
    #     t = int(input("Input torso: "))
    #     ra = int(input("Input right arm: "))
    #     la = int(input("Input left arm: "))
    #     rl = int(input("Input right leg: "))
    #     ll = int(input("Input left leg: "))
    #     self.armor.set_armor_values(h, t, ra, la, rl, ll)

    
    def set_stats(self):
        INT = int(input("Input INT: "))
        REF = int(input("Input REF: "))
        TECH = int(input("Input TECH: "))
        COOL = int(input("Input COOL: "))
        ATTR = int(input("Input ATTR: "))
        LUCK = int(input("Input LUCK: "))
        MA = int(input("Input MA: "))
        BODY = int(input("Input BODY: "))
        EMP = int(input("Input EMP: "))
        self.stats.set_stat_values(INT, REF, TECH, COOL, ATTR, LUCK, MA, BODY, EMP)

class NPC:
    def __init__(self, armor_values: Character_Armor = None, stat_values: Character_Stats = None):
        if armor_values:
            self.armor = armor_values
        else:
            self.armor = Character_Armor()
        
        if stat_values:
            self.stats = stat_values
        else:
            self.stats = Character_Stats()


def stats_to_string(character: Character):
    # this looks a bit off if there are any two-digit stat values
    print("STATS for " + character.name + ":")
    print("  INT  [" + str(character.stats.INT) + "]  REF [" + str(character.stats.REF) + "] TECH [" + str(character.stats.TECH) + "] COOL [" + str(character.stats.COOL) + "]")
    print("  ATTR [" + str(character.stats.ATTR) + "] LUCK [" + str(character.stats.LUCK) + "]   MA [" + str(character.stats.MA) + "] BODY [" + str(character.stats.BODY) + "]")
    print("  EMP  [" + str(character.stats.EMP) + "] Humanity [" + str(character.stats.humanity) + "]")
    print("  BTM  [" + str(character.stats.BTM) + "], " + character.stats.body_type_str)
    print("  Run  [" + str(character.stats.run) + "m]" + " Leap [" + str(character.stats.leap) + "m]")
    print("  Lift [" + str(character.stats.lift) + "kgs / " + str(int(character.stats.lift * 2.20462)) + "lbs]" + "  Carry [" + str(character.stats.carry) + "kgs / " + str(int(character.stats.carry * 2.20462)) + "lbs]")
    print("  SAVE [" + str(character.stats.SAVE) + "] BTM [" + str(character.stats.BTM) + "]")

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
    damage_amt -= character.stats.BTM

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

sample_stats = Character_Stats(10, 10, 5, 3, 5, 6, 9, 4, 6)
bait = Character("Bait", 0, None, None, None, None, None, None, None, None, sample_stats)
stats_to_string(bait)
damage(bait, 45, "head", False)