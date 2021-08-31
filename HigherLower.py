from art import logo,vs
from gameData import data
import random
from replit import clear

print(logo)
score = 0
gameShouldContinue = True
account_B = random.choice(data)

# make the game repeatable
while gameShouldContinue:
    def format_data(account):
        """ how to format account data into a one line """
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return (f"{account_name} ,a {account_descr}, from {account_country}")


    def checkAnswer(guess, a_followers,b_followers):
        """Takes the user's guess and checks the follower counts of a and b to determine if the user is correct"""
        if a_followers>b_followers:
            return guess == "a"
        else:
            return guess == "b"

    #generate random account from game data
    account_A = account_B
    account_B = random.choice(data)
    while account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Against B: {format_data(account_B)}")

    # ask the user to guess
    user_guess = input("Who has more followers?.  'a' or 'b' " ).lower()
    # check if user is correct
    ## get follower count
    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]
    ## if statement to check if user is correct
    is_correct = checkAnswer(user_guess,a_follower_count,b_follower_count)
    clear()
    print(logo)

    # give user a feedback
    #keep scoring
    if is_correct:
        score +=1
        print(f"You're right! Current Score: {score}")
    else:
        gameShouldContinue = False
        print(f"You're wrong! Final score: {score}")




# making accounts at position B become an account at position A

# clear the screen 
