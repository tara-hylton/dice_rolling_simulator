import random

def roll_dice(sides):

    match sides:
        case "4":
            print(random.randint(1, 4))
        case "6":
            print(random.randint(1, 6))
        case "8":
            print(random.randint(1, 8))
        case "10":
            print(random.randint(1, 10))
        case "12":
            print(random.randint(1, 12))
        case "20":
            print(random.randint(1, 20))
        case _:
            print("Not a valid choice, roll again")
print("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided")
sides = input()
roll_dice(sides)
while True:
    answer = input("Would you like to roll again? y/n\n").lower()
    if answer in ("y"):
        print("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided")
        sides = input()
        roll_dice(sides)
    elif answer in ("n"):
        print("May all of your rolls be critical. Goodbye.")
        break
    else:
        print("Not a valid choice. Would you like to roll again?")







#print(random.randint(1, 6))