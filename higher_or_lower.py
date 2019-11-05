import random

# Yanira Manzano & Mohamed Bagayoko
# Higher or Lower Game
# November 5 2019


def introduction():
    print("Hello user. My name is the dealer. Please enter your username:")
    username = input("> ")
    print(f"Welcome to Higher or Lower, {username}!")


def rules():
    print("""Do you want me to explain the rules?
(Enter 1 for Yes/ 2 for No)""")
    rule = int(input("> "))
    if rule == 1:
        print("""----------------------------------------------------------
You will start off with 30 point total. I will draw a number between 7-14. 
I will then reveal the number to you. Then this is where it gets interesting! 
I will draw a second number between 1-21. However, I will not reveal the number immediately. 
This is where you will step in. You will then have to guess if the second number is higher or lower than the first number. 
If answered correctly, the second number that you guessed will add itself to your total point count
If you lose, you will lose the amount of points the second number was rolled. Go bellow zero and you lose the game!
The goal is to get at least a 61 point total to win!
Now let's start the game!""")
        print("(Input anything to continue)")
        input("> ")
    elif rule == 2:
        print("Ok let's get started then!")
        print("(Input anything to continue)")
        input("> ")


def gameplay():
    go_ahead = True
    point_mark = 30 
    if point_mark == 61:            # Winning total
        print("You win the game!!!")
        go_ahead = False            # Game Continuation
    print("Ladies and gentlemen it's showtime!")
    while go_ahead:
        first_card = random.randint(7, 14)      # First Card
        print(f"Your first card is: {first_card}")
        print("(Input anything to continue)")
        input("> ")
        print("""Now Im am about to reveal the second card. 
Do you think its higher or lower than the first card?
(Enter 1 for high/ 2 for low)""")
        higher_lower = int(input("> "))
        if higher_lower == 1:
            print("""You chose higher. Are you sure about this?
(Input anything to continue)""")
            input("> ")
        elif higher_lower == 2:
            print("""You chose lower. Are you sure about this?
(Input anything to continue)""")
            input("> ")
        second_card = random.randint(1, 21)
        print(f"Ok then! Your second card is: {second_card}")
        new_mark = 30
        new_mark2 = 30
        if second_card > first_card:
            print(f"The second card ({second_card}) is higher than the first card ({first_card})")
            if higher_lower == 1:
                print("You were right!")
                print(f"Your point total is now a {new_mark}")
                print("We will keep going.")
                go_ahead = True
            if higher_lower == 2:
                print("You were wrong!")
                print(f"Your point total is now a {new_mark2}")
                print("We will keep going.")
                go_ahead = True
        if second_card < first_card:
            print(f"The second card ({second_card}) is lower than the first card ({first_card}).")
            if higher_lower == 1:
                print("You were wrong!")
                print(f"Your point total is now a {new_mark2}")
                print("We will keep going.")
                go_ahead = True
            if higher_lower == 2:
                print("You were right!")
                print(f"Your point total is now a {new_mark}")
                print("We will keep going.")
                go_ahead = True
        if second_card == first_card:
            print(f"The second card ({second_card}) was the same as the first card ({first_card}).")
            print("We have a draw! Your point total will not change.")
            print(f"Your point total remains as the same")
            print("We will keep going.")
            go_ahead = True



introduction()
rules()
gameplay()








