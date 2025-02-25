# HWST1276 - Zeef van Eratosthenes
#
# Lees een geheel getal in (int) als bovengrens. Je mag aannemen dat een positief getal zal worden ingelezen. Druk vervolgens alle getallen af tot en met die bovengrens die een priemgetal zijn. Een priemgetal is er een die enkel deelbaar is door 1 en zichzelf. Gebruik hiervoor de zeef van Eratosthenes. Deze zeef redeneert dat als een priemgetal is gevonden alle veelvouden van dat priemgetal mogen geschrapt worden omdat ze geen priemgetal meer kunnen zijn. Die veeldouden hebben immers het gevonden priemgetal als deler. Begin de zeef bij 2 en z'n veelvouden. 1 nemen we wel in het antwoord op, hoewel het strikt gezien geen priemgetal is!
#
# Tip: gebruik een bool tabel als zeef om getallen al dan niet als priem te markeren. De getallen zelf zijn dan de indexen van de cellen.
#
# Invoer
# Een positief geheel getal als bovengrens.
#
# Uitvoer
# Alle priemgetallen tot en met die bovengrens, gescheiden door een spatie. Achteraan mag een extra spatie staan als er getallen werden afgedrukt. Geen nieuwe lijn nemen!
#
# Voorbeelden
# Invoer:
# 14
#
# Uitvoer:
# 1 2 3 5 7 11 13<spatie>
