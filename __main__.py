import character # comes with character_armor and character_stats
import items


print("imports are compiling")

glowstick = items.Gear(name="Glowstick", cost=5.50, description="Exactly what you think it is.", type="Utility", notes="")
print(glowstick.name, glowstick.description)