#visi saxelic mtavrdeba i ze daiweros cool

import random
detachments=["dato mgeladze","vano motiashvili","davit janashia","aleqsandre katsarava","lasha wamalaidze","ilia wiklauri","nini nozadze","nika chochia","gabriel gogadze","sandro bochorishvili","dato jachvadze","giorgi gelashvili","muhammedali mamedov","sandro oqropiridze","erekle gochitashvili"]
randomizer=random.choice(detachments)
randomizer1=random.choice(detachments)
randomizer2=random.choice(detachments)

if randomizer[-1]=="i":
    print(randomizer1)
    print(randomizer+" cool")
    print(randomizer2)
elif randomizer1[-1]=="i":
    print(randomizer1+" cool")
    print(randomizer)
    print(randomizer2)
elif randomizer2[-1]=="i":
    print(randomizer2+" cool")
    print(randomizer1)
    print(randomizer)
else:
    print(randomizer+" sou bed imena")
    print(randomizer1+" sou bed imena")
    print(randomizer2+" sou bed imena")
