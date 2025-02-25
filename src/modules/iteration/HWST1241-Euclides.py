# HWST1241 - Euclides
#
# Lees twee positieve gehele getallen in (er mag verondersteld worden dat beide getallen positief zullen zijn!).
# Geef de grootste deler die beide getallen gemeenschappelijk hebben, ook wel de grootste gemene deler of ggd genoemd.
# Het bekendste en snelste algoritme hiertoe is dat van Euclides,
# waarbij herhaaldelijk het grootste getal wordt vervangen door het kleinste en het kleinste getal door
# de rest bij deling van het grootste door het kleinste getal.
# Als de rest nul wordt zal het kleinste getal die grootste gemene deler zijn.
#
# grootste	 	kleinste	 	grootste % kleinste
# 12
# 15	 	12
# 15
# 12	 	3
# 12
# 3	 	0
# Invoer
# Twee gehele getallen waarvan  het programma mag aannemen dat ze positief zijn.
#
# Uitvoer
# De grootste gemeenschappelijke deler van beide getallen. Geen nieuwe lijn!
#
# Voorbeelden
# Invoer:
# 225
# 15
#
# Uitvoer:
# 15
#
# Invoer:
# 15
# 12
#
# Uitvoer:
# 3