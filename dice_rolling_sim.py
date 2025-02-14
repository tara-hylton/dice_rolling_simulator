import random

#def is_number(input_value):
    #try:
        #float(input_value)
        #return True
    #except ValueError:
        #return False

#Function that rolls the dice, total roll is initialized to 0, so if a case is not matched, total roll will equal 0,
# meaning it is an invalid choice and will prompt an option to reroll the dice.
def roll_dice(sides,number_of_dice):
    i = 0
    total_roll = 0
    while i < number_of_dice:
        i += 1
        match sides:
            case 4:
                total_roll += random.randint(1, 4)
            case 6:
                total_roll += random.randint(1, 6)
            case 8:
                total_roll += random.randint(1, 8)
            case 10:
                total_roll += random.randint(1, 10)
            case 12:
                total_roll += random.randint(1, 12)
            case 20:
                total_roll += random.randint(1, 20)

    print(f'Your total roll of {number_of_dice} - {sides} sided dice is: {total_roll}')


#Input for roll of dice, also verifies that input is a positive integer.
def get_input(input_value):
    input_value = input("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n")
    if input_value.isnumeric():
        sides = int(input_value)
        print("How many dice are you rolling?")
        input_value = input()
        if input_value.isnumeric():
            number_of_dice = int(input_value)
            roll_dice(sides,number_of_dice)
        else:
            print("Your choice is invalid.")
    else:
        print("Your choice is an invalid.")

get_input(input)

#Reroll ask.
while True:
    answer = input("Would you like to roll again? y/n\n").lower()
    if answer in "y":
        get_input(input)
    elif answer in "n":
        print("May all of your rolls do max damage.")
        break
    else:
        print("Not a valid choice. Would you like to roll again?")







