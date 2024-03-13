# Spaces between each prompt were added for ease of reading
print("Welcome to Jasmine's Cafe!")
print("==========================")
print("Who's today's order for?")
name = input("Name: ")
print()
print("Welcome", name,"!")
print("==========================")

# This section displays the price of each item
# and requests the desired amount of product

print ("Choclate Chip Muffins are $2.35 per.")
muffins = int(input ("How many muffins do you want? "))

print()
print ("--------------------------")
print()

print ("Sliced Banana Bread is $2.50 per slice")
breadSlices = int(input ("How many slices do you want? "))

print()
print ("--------------------------")
print()
                    
print ("Each 15oz cup of coffee costs $3.75")
coffeeCups = int(input ("How many cups of coffee do you want? "))

print()
print ("--------------------------")
print()

print ("Each 15oz cup of lemonade costs $4.25")
lemonadeCups = int(input ("How many cups of lemonade do you want? "))

print()
print ("--------------------------")
print()

# This section is the calculating and receipt printing
muffinCost = muffins * 2.30
breadCost = breadSlices * 2.80
coffeeCost = coffeeCups * 3.75
lemonadeCost = lemonadeCups * 4.25
total = muffinCost + breadCost + coffeeCost + lemonadeCost
tax = total * .06
taxedTotal = 1.06 * total
print()
print()
# Each if-else statement is used to preserve grammar
# even when the amount of items are varied between
# single and bulk orders
print("***********************************")
print("          Jasmine's Cafe          ")

if muffins == 1:
    print ("1 muffin for $ 2.30")
else:
    if muffins >= 1:
        print (muffins, "muffins: $", muffinCost)
print()
if breadSlices == 1:
    print("1 slice of banana bread: $ 2.80")
else:
    if breadSlices >= 1:
        print(breadSlices, "slices of banana bread: $" , breadCost)
print()
if coffeeCups == 1:
    print("1 cup of coffee: $ 3.75")
else:
    if coffeeCups >= 1:
        print(coffeeCups, "cups of coffee: $",coffeeCost)
print()
if lemonadeCups == 1:
    print("1 cup of lemonade: $ 4.25")
else:
    if lemonadeCups >= 1:
        print(lemonadeCups, "cups of lemonade: $",lemonadeCost)
print()
print("6% tax: $", tax)
print("--------------------------")
print("Total: $",taxedTotal)
print("***********************************")
print("Thank you for orsering at Jasmine's Cafe!")

# I do ask that I am reffered to as Jasmine
# and addressed by She/Her pronouns. This
# is my way of coming out. I also had a
# little fun with the assignment. Sorry if
# it's not appropriate.
