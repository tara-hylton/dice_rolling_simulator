import random



def roll_dice(sides,number_of_dice):
    i = 0
    total_roll = 0
    while i < number_of_dice:
        i += 1
        match sides:
            case "4":
                total_roll += (random.randint(1, 4))
            case "6":
                total_roll += (random.randint(1, 6))
            case "8":
                total_roll += (random.randint(1, 8))
            case "10":
                total_roll += (random.randint(1, 10))
            case "12":
                total_roll += (random.randint(1, 12))
            case "20":
                total_roll += (random.randint(1, 20))

    if total_roll == 0:
        print("That choice is not valid.")
    else:
        print(f'Your total roll of {number_of_dice} - {sides} sided dice is: {total_roll}')

print("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n")
sides = input()
print("How many dice are you rolling?")
number_of_dice = int(input())
roll_dice(sides,number_of_dice)
while True:
    answer = input("Would you like to roll again? y/n\n").lower()
    if answer in ("y"):
        print("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n")
        sides = input()
        print("How many dice are you rolling?\n")
        number_of_dice = int(input())
        roll_dice(sides,number_of_dice)
    elif answer in ("n"):
        print("May all of your rolls be critical. Goodbye.")
        break
    else:
        print("Not a valid choice. Would you like to roll again?")







