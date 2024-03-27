# Sausages are in packs of 10
# Buns are in packs of 8
# Program needs to calculate the amount of packages
# required for each hotdog
import math

def dogCalc (x):
    dogsNeeded = x
    dogsLeft = (10 - (dogsNeeded % 10))
    if (dogsLeft > 0):
        dogPacks = math.ceil(dogsNeeded / 10)
        print("You need", dogPacks, "packs of hotdogs")
        print("[Warning: There will be", dogsLeft, "leftover dogs]")
    else:
        dogPacks = (dogsNeeded / 10)
        print("You need", dogPacks, "packs of hotdogs")

def bunCalc (x):
    bunsNeeded = x
    bunPacks = math.ceil(bunsNeeded / 8)
    bunsLeft = (8 - (bunsNeeded % 8))
    if (bunsLeft > 0):
        print("You need", bunPacks ," packs of buns")
        print("[Warning: You'll have", bunsLeft, "buns leftover]")
    else:
        print("You need", bunPacks, "packs of buns")

dogEaters = int(input("Please enter the number of attendees \n"))
print()
dogsEaten = int(input("How many dogs will a person eat? \n"))
totalDogs = (dogEaters * dogsEaten)
print("You need", totalDogs, "hotdogs to feed everyone")

dogCalc(x = totalDogs)
bunCalc(x = totalDogs)
