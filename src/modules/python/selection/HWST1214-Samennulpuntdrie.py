getal1 = float(input())
getal2 = float(input())
if abs((getal1 + getal2) - 0.3) < 1e-9:
    print("gelijk", end="")
else:
    print("ongelijk", end="")