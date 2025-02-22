basis = int(input())
while basis <= 0:
    basis = int(input())

if basis % 2 == 0:
    aantalLijnen = basis // 2
else:
    aantalLijnen = basis // 2 + 1

Lijn = 1

while Lijn <= aantalLijnen:
    whitSpacesLeft = 0
    while whitSpacesLeft + Lijn < aantalLijnen:
        print(" ", end="")
        whitSpacesLeft += 1
    aantalSterren = 0
    aantalSterOneven = 0
    while aantalSterren < Lijn:
        if basis % 2 != 0:
            if aantalSterOneven < 1:
                print("*", end="")
                aantalSterOneven += 1
            else:
                print("**", end="")
                aantalSterren += 1

        else:
            print("**", end="")
            aantalSterren += 1
    whitSpacesRight = 0
    while whitSpacesRight + Lijn < aantalLijnen:
        print(" ", end="")
        whitSpacesRight += 1
    print()
    Lijn += 1

#
#     **
#    ****
#   ******
#  ********
# **********
#
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

#
# aantalSterren = 0
# if hoogte % 2 != 0:
#     print("*", end="")
# else:
#     print("**", end="")
# print()
# if hoogte % 2 == 0:
#     aantalWhiteSpaces = hoogte // 2 - 1
# else:
#
#     aantalWhiteSpaces = hoogte // 2
# #
# # while aantalWhiteSpaces != 0:
# #     print("!", end="")
# #     aantalWhiteSpaces -=1
#
#
# while aantalSterren < aantalLijnen:
#
#     print("**", end="")
#     aantalSterren += 2
# # while aantalWhiteSpaces != 0:
# #     print(" ", end="")
# #     aantalWhiteSpaces -=1