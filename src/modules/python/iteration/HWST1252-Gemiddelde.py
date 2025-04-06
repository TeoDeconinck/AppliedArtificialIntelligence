getal = float(input())
totaal = 0
counter = 0
while getal != 0:
    totaal = totaal + getal
    counter += 1
    getal = float(input())
if counter == 0:
    print("geen data", end="")
else:
    print(round(totaal / counter, 4), end="")