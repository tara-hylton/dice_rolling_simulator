import random


#Function that rolls the dice, total roll is initialized to 0, so if a case is not matched, total roll will equal 0,
# meaning it is an invalid choice and will prompt an option to reroll the dice.
def roll_dice(sides,number_of_dice):
    i = 0
    total_roll = 0
    while i < number_of_dice:
        i += 1
        match sides:
            case "4":
                total_roll += random.randint(1, 4)
            case "6":
                total_roll += random.randint(1, 6)
            case "8":
                total_roll += random.randint(1, 8)
            case "10":
                total_roll += random.randint(1, 10)
            case "12":
                total_roll += random.randint(1, 12)
            case "20":
                total_roll += random.randint(1, 20)
    if total_roll != 0:
        print(f'Your total roll of {number_of_dice} - {sides} sided dice is: {total_roll}')
    else:
        print("Your choice is not valid.")

#Initial input for roll of dice.
print("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n")
sides = input()
print("How many dice are you rolling?")
number_of_dice = int(input())
roll_dice(sides,number_of_dice)

#Reroll ask.
while True:
    answer = input("Would you like to roll again? y/n\n").lower()
    if answer in "y":
        print("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n")
        sides = input()
        print("How many dice are you rolling?\n")
        number_of_dice = int(input())
        roll_dice(sides,number_of_dice)
    elif answer in "n":
        print("May all of your rolls do max damage.")
        break
    else:
        print("Not a valid choice. Would you like to roll again?")







