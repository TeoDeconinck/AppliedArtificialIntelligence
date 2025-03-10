basis = int(input())
while basis <= 0:
    basis = int(input())

Lijnen = 1
while Lijnen <= basis:
    aantlSterren = basis - Lijnen + 1
    while aantlSterren > 0:
        print("**", end="")
        aantlSterren -= 2
    print()
    Lijnen += 1




















# Vraag met een programma de basis van een rechthoekige gelijkbenige driehoek. Beeld deze vervolgens af met '*' symbolen. De driehoek begint met de basis en loopt gelijkbenig naar beneden in een top. Na het afdrukken neem je een nieuwe lijn.
#
# Als iemand een negatief getal of nul opgeeft dan blijf je aandringen op strikt een positief getal.
#
# Invoer
# Een geheel getal (int) als basis. Je blijft een getal opvragen tot je een geheel getal hebt dat strikt positief is.
#
# Uitvoer
# De gelijkbenige rechthoekige driehoek, met z'n basis bovenaan, sluit gelijkbenig naar beneden tot aan z'n top, gevolgd door een nieuwe lijn. Opgelet, door de schermkarakteristieken van de console dien je een driehoek met een even basis met twee '*' symbolen te eindigen.
#
# Voorbeeld
# Invoer:
# -3
# 0
# 5
#
# Uitvoer:
# *
# *
# *
# *
# *
#
# *
# *
# *
#
#
# *
#
# (basis = 5, neem een nieuwe lijn na het afdrukken van de driehoek!)
# Invoer:
# -3
# 0
# 4
#
# Uitvoer:
# *
# *
# *
# *
#
# *
# *
#
# (basis = 4, neem een nieuwe lijn na het afdrukken van de driehoek!)