import random 
crew_leaders = ['kruashvili', 'amiranashvili', 'tyeshelashvili', 'janezashvili', 'molodini', 'kereselidze', 'kurtanidze']

randomizer=random.choice(crew_leaders)
randomizer1=random.choice(crew_leaders)
randomizer2=random.choice(crew_leaders)
while randomizer==randomizer1 or randomizer==randomizer2 or randomizer1==randomizer2:
    randomizer=random.choice(crew_leaders)
    randomizer1=random.choice(crew_leaders)
    randomizer2=random.choice(crew_leaders)

print(randomizer)
print(randomizer1)
print(randomizer2)
