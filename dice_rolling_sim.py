import random


#Function that rolls the dice, total roll is initialized to 0 and will print total roll at end.
def roll_dice(n_sided,number_of_dice):
    i = 0
    total_roll = 0
    while i < number_of_dice:
        i += 1
        match n_sided:
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
                if number_of_dice == 1 and total_roll == 20:
                    print("Critical Hit")
                elif number_of_dice == 1 and total_roll == 1:
                    print("Oh no! You fumbled!")
    print(f'Your total roll of {number_of_dice} - {n_sided} dice is {total_roll}!')
    if total_roll / number_of_dice < (n_sided / 2):
        print("Bad luck my friend")
    else:
        print("Excellent roll "+ your_name)

your_name = input("Welcome to the fantasy dice roller simulator! What is your name?\n")


#Input for roll of dice and verifies the input is valid.
def get_input(input_value):
    random_error = ["You have failed!", "You have doomed us all!", "You hit a trap!",
                    "Oh no! You got drunk at the tavern!", "No one asked for a bard...",
                    "Time for a new dungeon master.", "You're not a barbarian!"]
    random_string_error = random.choice(random_error) #chooses random error message
    input_value = input(f'{your_name}, please choose which dice you would like to roll by entering the number of sides (one choice)?\n 4 sided\n 6 sided\n 8 sided\n 10 sided\n 12 sided\n 20 sided\n')
    if input_value.isnumeric() and (input_value != "0"): #ensures char is positive number and not equal to zero
        n_sided = int(input_value)
        list_of_dice = [4,6,8,10,12,20] #ensures number is in the list of dice
        if n_sided in list_of_dice:
            print("How many dice are you rolling?")
            input_value = input()
            if input_value.isnumeric() and input_value != "0":  #ensures char is positive number and not equal to zero
                number_of_dice = int(input_value)
                roll_dice(n_sided,number_of_dice)          #calls the function to roll the dice
            else:
                print(random_string_error)
        else:
            print(random_string_error)
    else:
        print(random_string_error)

get_input(input)   #calls the function to get the input

#Asks user if they would like to roll again and verifies input is valid.
while True:
    answer = input(f'Would you like to try again {your_name}? y/n\n').lower()
    if answer in "y":
        get_input(input)
    elif answer in "n":
        random_goodbye = ["May all of your rolls do max damage.",
                          "May all of your hits be critical.""May you always gain initiative over enemies.",
                          "May all of your knives be ogre slaying."]
        random_string_goodbye = random.choice(random_goodbye)   #chooses random goodbye message
        print(random_string_goodbye)
        break
    else:
        random_error = ["You have failed!", "You have doomed us all!", "You hit a trap!",
                        "Oh no! You got drunk at the tavern!", "No one asked for a bard...",
                        "We requested a new dungeon master.", "You're not a barbarian!"]
        random_string_error = random.choice(random_error)     #chooses random error message
        print(random_string_error)







