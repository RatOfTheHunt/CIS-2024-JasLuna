import math

def addTen():
    print ("Enter a number:") 
    userNumber = int(input()) 
    number = userNumber + 10 
    return number 

def gender(): 
    female = False  
    print("Enter your gender (male or female):") 
    userGender = input() 
    if (userGender.lower() == "male"): 
        answer = False 
    else:
        answer = True 
    return answer
def rootNum():
    myNumber = int(input("Please enter a number \n"))
    while myNumber <= 0 :
        print("Please enter a positive number")
        myNumber = int(input())
    sqrNumber = math.sqrt(myNumber)
    print(myNumber, "has a root of", sqrNumber)
    return sqrNumber
def receiptTax():
    taxRate = .06
    subTotal = float(input("Please enter the subtotal \n"))
    total = round(subTotal + (subTotal * taxRate),2)
    print("Your total is $", total)
    

number = addTen()
sqrNumber = rootNum()
answer = gender()
receiptTax()
print(number)
print(sqrNumber)
print(answer)
