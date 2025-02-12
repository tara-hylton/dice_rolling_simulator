import random



def roll_dice(sides):
    i = 0
    total_roll = 0
    while i < number_of_dice:
        i += 1
        match sides:
            case "4":
                total_roll += (random.randint(1, 4))
            case "6":
                total_roll += (random.randint(1, 6))
                print(total_roll, i)
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

    print(total_roll, i)

print("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n")
sides = input()
print("How many dice are you rolling?")
number_of_dice = int(input())
roll_dice(sides)
while True:
    answer = input("Would you like to roll again? y/n\n").lower()
    if answer in ("y"):
        print("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n")
        number_of_dice = input("How many dice are you rolling?\n")
        sides = input()
        roll_dice(sides)
    elif answer in ("n"):
        print("May all of your rolls be critical. Goodbye.")
        break
    else:
        print("Not a valid choice. Would you like to roll again?")







