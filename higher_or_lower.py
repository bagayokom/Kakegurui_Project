import random

# Yanira Manzano & Mohamed Bagayoko
# Higher or Lower Game
# November 5 2019


def introduction():
    print("Hello user. My name is the dealer. Please enter your username:")
    username = input("> ")
    print(f"""Ladies and gentlemen it's showtime!
Welcome to Higher or Lower {username}!""")

def rules():
    print("""Do you want me to explain the rules?
(Enter 1 for Yes/ 2 for No)""")
    rule = int(input("> "))
    if rule == 1:
        print("""----------------------------------------------------------
You will start off with 30 point total. I will  draw a number between 10-21. 
I will then reveal the number to you. Then this is where it gets interesting! 
I will draw a second number between 10-21. However, I will not reveal the number immediately. 
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


introduction()
rules()






