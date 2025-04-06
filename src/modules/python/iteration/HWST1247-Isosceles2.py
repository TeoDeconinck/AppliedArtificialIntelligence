hoogte = int(input())
aantallijnen = 0


while hoogte <= 0:
    hoogte = int(input())

while aantallijnen < hoogte:
    aantalsterren = hoogte - aantallijnen

    aantalAfgedrukteSterren = 0
    while aantalAfgedrukteSterren < aantalsterren:
        print("*", end="")
        aantalAfgedrukteSterren += 1
    print()
    aantallijnen += 1