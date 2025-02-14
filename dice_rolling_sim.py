import random

#def is_number(input_value):
    #try:
        #float(input_value)
        #return True
    #except ValueError:
        #return False

#Function that rolls the dice, total roll is initialized to 0 and will print total roll at end.
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


#Input for roll of dice, also verifies that input is a positive integer, not zero, not a letter or character, and
def get_input(input_value):
    input_value = input("What die would you like to roll?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n")
    if input_value.isnumeric() and (input_value != "0"):
        sides = int(input_value)
        list_of_dice = [4,6,8,10,12,20]
        if sides in list_of_dice:
            print("How many dice are you rolling?")
            input_value = input()
            if input_value.isnumeric() and input_value != "0":
                number_of_dice = int(input_value)
                roll_dice(sides,number_of_dice)
            else:
                print("Your choice is invalid.")
        else:
            print("You can't read")
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







