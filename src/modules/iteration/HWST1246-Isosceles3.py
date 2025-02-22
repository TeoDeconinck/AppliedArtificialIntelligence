hoogte = int(input())


while hoogte <= 0:
    hoogte = int(input())

aantalLijnen = 1

while aantalLijnen <= hoogte:
    aantalSterren = 0

    aantalAfTeDrukkenSterren = hoogte - aantalLijnen + 1
    aantalWhiteSpaces = 0
    while aantalWhiteSpaces <= (hoogte - aantalAfTeDrukkenSterren -1):
        print(" ", end="")
        aantalWhiteSpaces += 1
    while aantalSterren < aantalAfTeDrukkenSterren:
        aantalWhiteSpaces = 0

        print("*", end="")
        aantalSterren += 1
    print()

    aantalLijnen += 1