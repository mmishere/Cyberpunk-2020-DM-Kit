class Character_Stats:
    def __init__(self, i, r, t, c, a, l, m, b, e):
        if (not i or not r or not t or not c or not a or not l or not m or not b or not e):
            print("All values must be inputted! INT, REF, TECH, COOL, ATTR, LUCK, MA, BODY, EMP.")
            return
        
        if (i < 0 or r < 0 or t < 0 or c < 0 or a < 0 or l < 0 or m < 0 or b < 0 or e < 0):
            print("A STAT value was less than 0. Invalid input, please try again.")
            return
        elif (i > 10 or r > 10 or t > 10 or c > 10 or a > 10 or l > 10 or m > 10 or b > 10 or e > 10):
            response = input("A stat value was greater than 10! Are you sure you want to continue? y/n")
            if (response == "n"):
                print("Response was no. Ending.")
                return
            else:
                print("Response was yes. Continuing!")

        self.INT = i
        self.REF = r
        self.TECH = t
        self.COOL = c
        self.ATTR = a
        self.LUCK = l
        self.MA = m
        self.BODY = b
        self.EMP = e

        # Derived stats:
        self.SAVE = b
        self.run = m * 3
        self.leap = (m * 3) / 4
        self.lift = b * 40
        self.carry = b * 10
        self.humanity = e * 10

        if (self.BODY <= 2):
            self.melee_modifier = -2
            self.body_type_str = "Very weak"
            self.BTM = 0
        elif (self.BODY <= 4):
            self.melee_modifier = -1
            self.body_type_str = "Weak"
            self.BTM = -1
        elif (self.BODY <= 7):
            self.melee_modifier = 0
            self.body_type_str = "Average"
            self.BTM = -2
        elif (self.BODY <= 9):
            self.melee_modifier = 1
            self.body_type_str = "Strong"
            self.BTM = -3
        elif (self.BODY == 10):
            self.melee_modifier = 2
            self.body_type_str = "Very strong"
            self.BTM = -4
        # after this, the only thing that changes is melee_modifier: see friday night firefight melee section for details
        elif (self.BODY <= 12):
            self.melee_modifier = 4
            self.body_type_str = "Superhuman"
            self.BTM = -5
        elif (self.BODY <=  14):
            self.melee_modifier = 6
            self.body_type_str = "Superhuman"
            self.BTM = -5
        elif (self.BODY >= 15):
            self.melee_modifier = 8
            self.body_type_str = "Superhuman"
            self.BTM = -5

    # set_stat_values is a copy of __init__(), so the code is mostly the same; if you change something above, change it here as well
    def set_stat_values(self, i, r, t, c, a, l, m, b, e):
        if (not i or not r or not t or not c or not a or not l or not m or not b or not e):
            print("All values must be inputted! INT, REF, TECH, COOL, ATTR, LUCK, MA, BODY, EMP.")
            return
        
        if (i < 0 or r < 0 or t < 0 or c < 0 or a < 0 or l < 0 or m < 0 or b < 0 or e < 0):
            print("A STAT value was less than 0. Invalid input, please try again.")
            return
        elif (i > 10 or r > 10 or t > 10 or c > 10 or a > 10 or l > 10 or m > 10 or b > 10 or e > 10):
            response = input("A stat value was greater than 10! Are you sure you want to continue? y/n")
            if (response == "n"):
                print("Response was no. Ending.")
                return
            else:
                print("Response was yes. Continuing!")

        self.INT = i
        self.REF = r
        self.TECH = t
        self.COOL = c
        self.ATTR = a
        self.LUCK = l
        self.MA = m
        self.BODY = b
        self.EMP = e

        # Derived stats:
        self.SAVE = b
        self.run = m * 3
        self.leap = (m * 3) / 4
        self.lift = b * 40
        self.carry = b * 10
        self.humanity = e * 10

        if (self.BODY <= 2):
            self.melee_modifier = -2
            self.body_type_str = "Very weak"
            self.BTM = 0
        elif (self.BODY <= 4):
            self.melee_modifier = -1
            self.body_type_str = "Weak"
            self.BTM = -1
        elif (self.BODY <= 7):
            self.melee_modifier = 0
            self.body_type_str = "Average"
            self.BTM = -2
        elif (self.BODY <= 9):
            self.melee_modifier = 1
            self.body_type_str = "Strong"
            self.BTM = -3
        elif (self.BODY == 10):
            self.melee_modifier = 2
            self.body_type_str = "Very strong"
            self.BTM = -4
        # after this, the only thing that changes is melee_modifier: see friday night firefight melee section for details
        elif (self.BODY <= 12):
            self.melee_modifier = 4
            self.body_type_str = "Superhuman"
            self.BTM = -5
        elif (self.BODY <=  14):
            self.melee_modifier = 6
            self.body_type_str = "Superhuman"
            self.BTM = -5
        elif (self.BODY >= 15):
            self.melee_modifier = 8
            self.body_type_str = "Superhuman"
            self.BTM = -5