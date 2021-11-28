import character
import character_stats


# def test_stats_constructor():
#     #constructor with invalids: too large, too small


#     # # default constructor
#     # defaultStats = character_stats.Stats()
#     # assert (defaultStats.INT == 0 and defaultStats.REF == 0 and defaultStats.TECH == 0 and defaultStats.COOL == 0 and defaultStats.ATTR == 0 and defaultStats.LUCK == 0 and defaultStats.MA == 0 and defaultStats.BODY == 0 and defaultStats.EMP == 0), "Default stat values don't work!"
#     # assert (defaultStats.SAVE == 0 and defaultStats.run == 0 and defaultStats.leap == 0 and defaultStats.lift == 0 and defaultStats.carry == 0 and defaultStats.humanity == 0 and defaultStats.BTM == 0 and defaultStats.body_type_str == "Very Weak" and defaultStats.melee_modifier == -2), "Default derived stats don't work!"

#     # constructor with all different values
#     stats1 = character_stats.Stats(5, 3, 9, 1, 2, 4, 6, 8, 7)
#     assert (stats1.INT == 5 and stats1.REF == 3 and stats1.TECH == 9 and stats1.COOL == 1 and stats1.ATTR == 2 and stats1.LUCK == 4 and stats1.MA == 6 and stats1.BODY == 8 and stats1.EMP == 7), "Different stat values don't work!"
#     # assert (stats1.SAVE == 8 and stats1.run == 18 and stats1.leap == 4.5 and stats1.lift == 320 and stats1.carry == 80 and stats1.humanity == 70 and stats1.BTM == -3 and stats1.body_type_str == "Strong" and stats1.melee_modifier == 2), "Different derived stats don't work!"

#     assert stats1.SAVE == 8,   "SAVE"
#     assert stats1.run  == 18,  "run"
#     assert stats1.leap == 4.5, "leap"
#     assert stats1.lift == 320, "lift"
#     assert stats1.carry == 80, "carry"
#     assert stats1.humanity == 70, "humanity"
#     assert stats1.BTM == -3, "BTM"
#     assert stats1.body_type_str == "Strong", "Body type str"
#     assert stats1.melee_modifier == 1, "melee modifier"




def test_stat_str() -> None:
    # # default char
    # defaultStats = character_stats.Stats()
    # defaultCharacter = character.Character()
    # defaultCharacter.stats = defaultStats
    # defaultString = """
    # INT  [0]  REF [0] TECH [0] COOL [0]
    # ATTR [0] LUCK [0]   MA [0] BODY [0]
    # EMP  [0] Humanity [0]
    # Run  [0m] Leap [0m]
    # Lift [0kgs / 0lbs] Carry [0kgs / 0lbs]
    # SAVE [0] BTM [0] Melee Modifier [-2], Very Weak
    # """
    # assert character.stats_to_string(defaultCharacter) == defaultString

    # valid char
    stats1 = character_stats.Stats(5, 3, 9, 1, 2, 4, 6, 8, 7)
    stats1Str = character.serialize_stats(stats1)
    stats1Character = character.Character()
    stats1Character.stats = stats1Str
    stats1Character.handle = "A Character"
    stats1String = """
    A Character
    INT  [5]  REF [3] TECH [9] COOL [1]
    ATTR [2] LUCK [4]   MA [6] BODY [8]
    EMP  [7] Humanity [70]
    Run  [18m] Leap [4.5m]
    Lift [320kgs / 705lbs] Carry [80kgs / 176lbs]
    SAVE [8] BTM [-3] Melee Modifier [1], Strong
    """
    assert character.stats_to_string(stats1Character) == stats1String
