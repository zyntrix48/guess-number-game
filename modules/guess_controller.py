def guess_number(number, guessed_number):
    if number == guessed_number:
        print("You guessed the number!")
    elif number > guessed_number:
        print("Less!")
    else: 
        print("More!")