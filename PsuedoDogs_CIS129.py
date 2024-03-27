##// main module                                 
##Module main()
import math
def main():
##   // Local variable for the total number of hot dogs needed.
##   Declare Integer total
##
##   // Input --------------------------------------
##   // Get the total number of hot dogs needed.
    total = getTotalHotDogs()
##
##   // Processing ----------------------------------
##   // Named constants for the package sizes
##   Constant Integer DOGS = 10   // Hot dogs in a package
    dogs = 10
##   Constant Integer BUNS = 8    // Hot dog buns in a package
    buns = 8
##
##   // Local variables
##   Declare Integer dogsLeft  // Left over hot dogs
##   Declare Integer bunsLeft  // Left over hot dog buns
##   Declare Integer minDogs   // Minimum packages of hot dogs
##   Declare Integer minBuns   // Minimum packages of hot dog buns
##
##   // Calculate the number of left over hot dogs.
##   Set dogsLeft = (DOGS - total MOD DOGS) MOD DOGS
    dogsLeft = (dogs - total % dogs) % dogs
##
##   // Calculate the minimum number of packages of hot dogs.
##   Set minDogs = Math.ceil(total / DOGS)
    minDogs = math.ceil(total/dogs)
##
##   // Calculate the number of left over hot dog buns.
##   Set bunsLeft = (BUNS - total MOD BUNS) MOD BUNS
    bunsLeft = (buns - total % buns) % buns
##
##   // Calculate the minimum number of packages of hot dogs buns.
##   Set minBuns = Math.ceil(total / BUNS)
    minBuns = math.ceil(total/buns)
##
##   // Output ----------------------------------------
##   // Display the results.
    showResults(dogsLeft,minDogs,bunsLeft,minBuns)
##   Call showResults(dogsLeft, minDogs, bunsLeft, minBuns)
##End Module

def getTotalHotDogs():
##
##   // Local variables
##   Declare Integer people   // Number of people attending
##   Declare Integer hotDogs  // Hot dogs per person
##
##   // Get the number of people attending the cookout.
    print("Enter the number of people attending the cookout: ")
    people = int(input())
##
##   // Get the number of hot dogs each person will be given.
    print(" Enter the number of hot dogs for each person: ")
    hotDogs = int(input())
##
##   // Calculate the total number of hot dogs needed.
    total = people * hotDogs
    return total
##End Function


def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    
##
##   // Display the minimum packages of hot dogs needed.
    print("Minimum packages of hot dogs needed: ", minDogs)
##
##   // Display the minimum packages of buns needed.
    print("Minimum packages of hot dog buns needed: ", minBuns)
##
##   // Display the number of hot dogs left over.
    print("Hot dogs left over: ", dogsLeft)
##
##   // Display the number of hot dog buns left over
    print("Hot dog buns left over: ", bunsLeft)
##End Module
main()
