hoogte = int(input())
breedte = int(input())

aantalLijnen = 0

if (hoogte > 0) and (breedte > 0):
    while aantalLijnen < hoogte:
        aantalSterren = 0
        while aantalSterren < breedte:
            print("*", end="")
            aantalSterren += 1
        if aantalSterren > 0:
            print()
        aantalLijnen +=1

