# HWST1270 - Reverse sequence hell
#
# Schrijf een programma dat honderd getallen (int) inleest en die onder elkaar in omgekeerde volgorde terug afdrukt.
# Na het afdrukken van het laatste getal wordt ook een nieuwe lijn genomen.
#
# Invoer
# Honderd gehele getallen.
#
# Uitvoer
# Dezelfde 100 gehele getallen, onder elkaar, in omgekeerde volgorde. Er wordt afgesloten met een nieuwe lijn.
#
# Voorbeeld
# Invoer:
# 1
# 2
# ...
# 99
# 100
#
# Uitvoer:
# 100
# 99
# ...
# 2
# 1
# <nieuwe lijn>

inGelezenGetallen = [] * 100

i = 0

while i <= len(inGelezenGetallen):
    inGelezenGetallen[i] = int(input())
    i +=1

i = len(inGelezenGetallen) -1
while i >= 0:
    print(inGelezenGetallen[i])
    i -= 1