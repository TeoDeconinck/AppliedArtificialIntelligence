import math
straal = float(input())
if straal >= 0:
    print(math.pi * straal ** 2, end="")
else:
    print("?", end="")