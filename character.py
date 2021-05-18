import character_stats
import character_armor

# also need to track eb
class Character:
    def __init__(self, armor_values = None, stat_values = None):
        if armor_values:
            self.armor = armor_values
        else:
            self.armor = character_armor.Character_Armor()
        
        if stat_values:
            self.stats = stat_values
        else:
            self.stats = character_stats.Character_Stats()
    

    # def set_armor(self, h = None, t = None, ra = None, la = None, rl = None, ll = None):
    #     self.armor = character_armor.set_stats(h, t, ra, la, rl, ll

    def set_armor(self):
        h = int(input("Input head: "))
        t = int(input("Input torso: "))
        ra = int(input("Input right arm: "))
        la = int(input("Input left arm: "))
        rl = int(input("Input right leg: "))
        ll = int(input("Input left leg: "))
        self.armor.set_armor_values(h, t, ra, la, rl, ll)

    
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


def stats_to_string(character):
    pass

def armor_to_string(character):
    pass



# arm = character_armor.Character_Armor(1, 2, 3, 4, 5, 6)
# me = Character(arm, None)
# print(me.armor.left_arm)
# me.set_armor()
# print(me.armor.left_arm)