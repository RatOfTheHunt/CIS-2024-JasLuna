# These are the variables that are used in this program

monthlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0

# This prompts the user to input sales made this month
monthlySales = float(input("Please report this month's sales: "))

# This calculates the amount of store bonus to give out based
# the amount of sales made in the month
if monthlySales >= 110000: 
    storeAmount = 6000 
elif monthlySales >= 100000:
    storeAmount = 5000 
elif monthlySales >= 90000: 
    storeAmount = 4000		 
elif monthlySales >= 80000: 
    storeAmount = 3000 
else: 
    storeAmount = 0

# This collects and calculates the % amount of increase in sales
salesIncrease = float(input("Please input sales increase percent")) 
salesIncrease = salesIncrease / 100

# This code determines the amount of bonus employees get
if salesIncrease >= .05: 
    empAmount = 75 
elif salesIncrease >= .04: 
    empAmount = 50 
elif salesIncrease >= .03: 
    empAmount = 40 
else: 
    empAmount = 0

# This code prints the bonus information 

print("The store bonus amount is $", storeAmount) 
print("The employee bonus amount is $", empAmount)

if (storeAmount == 6000 ) and (empAmount == 75): 
    print('Congrats! You have reached the highest bonus amounts possible! ') 
