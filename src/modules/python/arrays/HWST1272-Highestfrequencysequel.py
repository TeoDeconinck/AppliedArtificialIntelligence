# Schrijf een programma dat getallen (int) inleest tussen 0 en 99.
# Van zodra een getal buiten dit interval valt worden geen getallen meer gevraagd en wordt dat laatste getal ook niet meer verwerkt
# (anders gesteld is alles buiten [0,99] dus sentinel).
# Druk het getal af dat het meest is voorgekomen maar neem geen nieuwe lijn.
# Als er geen geschikte getallen werden ingegeven dan wordt 0 afgedrukt als antwoord.
#
# Invoer
# Gehele getallen in het interval [0,99]. Stop van zodra je iets krijgt dat daar buiten valt.
#
# Uitvoer
# Het getal dat het meest voorkwam in de invoerstroom. Als bepaalde getallen evenveel voorkwamen dan druk je enkel het grootste af.
# Nul in het geval er geen geschikte getallen werden opgegeven. Neem na het afdrukken geen nieuwe lijn.
#
# Voorbeeld
# Invoer:
# 3
# 2
# 1
# 3
# 5
# 3
# 1
# -10
#
# Uitvoer:
# 3
#
# Invoer:
# 1
# 3
# 2
# 1
# 3
# 5
# 3
# 1
# 354
#
# Uitvoer:
# 3

frequentieTabel = [0] * 100
getal = int(input())

while 0 <= getal < 100:
    frequentieTabel[getal] += 1
    getal = int(input())

MeestFrequenteGetal = 0
i = 0
while i < 100:
    if frequentieTabel[i] => frequentieTabel[MeestFrequenteGetal]: MeestFrequenteGetal = i
    i += 1
if MeestFrequenteGetal == 0:
    print(0, end = '')
else:
    print(MeestFrequenteGetal, end = '')