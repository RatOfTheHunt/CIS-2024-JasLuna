
# ValueError Is it's own standalone term!
# Try attempts to execute a section of code but doesn't crash everything if it's unsucessful
# Paired with except as well! Similar to the If-Else structure
# functions can have messages input into them via "(message)"


def main():
    while True:
        userNum = get_int("Enter a number \n")
        if (userNum % 2 == 0):
            print("Even Number")
        else:
            print("Odd Number")
        print("Try again?")
        continuity = input('input "y" to continue')
        if continuity.lower() != "y":
            break
def get_int(message):
    errorCount = 0
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("incorrect data type, please enter an integer")

main()
