class Character_Armor:
    # first, make an armor piece
    # then, apply it to the character

    # this is only really relevant if you want to make an NPC or something without worrying about specific items; in other words, default armor

    def __init__(self, h: int = None, t: int = None, ra: int = None, la: int = None, rl: int = None, ll: int = None):
        # either take in all or none
        if (not h and not t and not ra and not la and not rl and not ll):
            self.head = 0
            self.torso = 0
            self.right_arm = 0
            self.left_arm = 0
            self.right_leg = 0
            self.left_leg = 0
        elif (h and t and ra and la and rl and ll):
            print("Setting armor values")
            self.head = h
            self.torso = t
            self.right_arm = ra
            self.left_arm = la
            self.right_leg = rl
            self.left_leg = ll
        else:
            print("Input all values or no values; can't only have some")
    
    # takes in ints
    def set_armor_values(self, h: int, t: int, ra: int, la: int, rl: int, ll: int):
        if (h < 0 or t < 0 or ra < 0 or la < 0 or rl < 0 or ll < 0):
            print("An armor SP value was less than 0. Invalid input, please try again.")
            return False
        
        self.head = h
        self.torso = t
        self.right_arm = ra
        self.left_arm = la
        self.right_leg = rl
        self.left_leg = ll
        return True
    
    def set_head(self, h):
        if h < 0:
            print("Head SP value was less than 0. Invalid input, please try again.")
            return False
        self.head = h
        return True
    
    def set_torso(self, t):
        if t < 0:
            print("Torso SP value was less than 0. Invalid input, please try again.")
            return False
        self.torso = t
        return True
    
    def set_right_arm(self, ra):
        if ra < 0:
            print("Right arm SP value was less than 0. Invalid input, please try again.")
            return False
        self.right_arm = ra
        return True
    
    def set_left_arm(self, la):
        if la < 0:
            print("Left arm SP value was less than 0. Invalid input, please try again.")
            return False
        self.left_arm= la
        return True
    
    def set_right_leg(self, rl):
        if rl < 0:
            print("Right leg SP value was less than 0. Invalid input, please try again.")
            return False
        self.right_leg = rl
        return True
    
    def set_left_leg(self, ll):
        if ll < 0:
            print("Left leg SP value was less than 0. Invalid input, please try again.")
            return False
        self.left_leg = ll
        return True
