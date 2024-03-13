# Jose Luna
# Preferred Name : Jasmine
# Date: March 9 2024
# CIS 129 program
# Designed to record bottle colletion from a store over the course of a week
# and calculate the profits from them. Asks for another week after the days
# scheduled run out.

keepGoing = "y"
while keepGoing.lower() == "y":
    #Declares the variables used within the loop
    totalBottles = 0
    totalPayout = 0
    todayBottles = 0
    counter = 0
    loopAmount = 0

    #Collects and records bottle amount over the week.
    #Also calculates and displays payment and total bottles 
    print("Welcome to the bottle buy back program")
    counter = int(input("Please enter the amount of days today \n Note: Input a number between 1 and 7 "))
    print()
    print()
    print()
    while counter > 0:
        todayBottles = int(input("Please enter the amount of bottles collected today \n"))

        totalBottles = todayBottles + totalBottles
        counter = counter - 1
        loopAmount = loopAmount + 1
    
        print()
        print("Today's bottle count:" , todayBottles)
        print("Current week's bottle count:" , totalBottles)
        print("Current payout:" , totalPayout)
        print()

    
    #The results show how many bottles were collected over the week along with their profits 
    totalPayout = totalBottles * .10
    print()
    print("====== Results ======")
    print("Total Bottles \n", totalBottles)
    print()
    print("Total Payout \n $" , totalPayout)
    print()
    print("Days elapsed this week\n ",loopAmount)
    print()
    print()
    print('If you would like to enter a new week of data, enter "y"')
    keepGoing = input()
