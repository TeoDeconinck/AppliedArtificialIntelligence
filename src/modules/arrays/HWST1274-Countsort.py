# Schrijf een programma dat getallen (int) inleest tussen 0 en 99. Van zodra een getal buiten dit interval valt worden geen getallen meer gevraagd en wordt dat laatste getal ook niet meer verwerkt (anders gesteld is alles buiten [0,99] dus sentinel).Druk alle getallen af van klein naar groot gescheiden door spaties . Als er geen geschikte getallen werden ingegeven dan wordt gewoon een nieuwe lijn afgedrukt. Getallen die meerdere keren voorkomen worden in de sortering slecht één keer afgedrukt!
#
# Invoer
# Gehele getallen in het interval [0,99]. Stop van zodra je iets krijgt dat daar buiten valt.
#
# Uitvoer
# De ingegeven getallen van klein naar groot, gescheiden door spaties. Je neemt geen nieuwe lijn en drukt op het einde ook geen spatie meer af. In het geval er geen geschikte getallen werden opgegeven neem je wel en alleen een nieuwe lijn. Getallen worden dus niet herhaald!
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
# 1 2 3 5<geen nieuwe lijn>
#
# Invoer:
# 132
#
# Uitvoer:
# <nieuwe lijn>