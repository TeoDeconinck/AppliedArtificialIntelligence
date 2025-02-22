hoogte = int(input())


while hoogte <= 0:
    hoogte = int(input())

aantalLijnen = 1

while aantalLijnen <= hoogte:
    aantalSterren = 0

    aantalWhiteSpaces = hoogte - aantalLijnen
    while aantalWhiteSpaces != 0:
        print(" ", end="")
        aantalWhiteSpaces -=1
    while aantalSterren < aantalLijnen:
        print("*", end="")
        aantalSterren += 1
    print()

    aantalLijnen += 1