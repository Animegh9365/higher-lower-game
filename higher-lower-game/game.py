from tabnanny import check
from turtle import clear
from gamedata import data
from art import logo,vs
import random
import os

#get random data from random account
def randomAccount(data):
    """Get data from random account"""
    return random.choice(data)

#format random account to readable format

def format_data(account):
    """Format account into printable format: name,description and country"""
    acc_name=account["name"]
    acc_description=account["description"]
    acc_country=account["country"]
    return f"{acc_name},a {acc_description},from {acc_country}"


def check_answer(guess,a_followers,b_followers):
    # Use if statement if the user is correct
    """Take the users guess and follower counts and return if they got it right"""
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess=="b"




score=0
game_should_continue=True
account_A=random.choice(data)
account_B=random.choice(data)
# Make the game repeatable
while game_should_continue:
    print(logo)
    account_A=account_B
    account_B=random.choice(data)
    while account_A == account_B:
        account_B = random.choice(data) 
    print(f"Compare A: {format_data(account_A)}.")
    print(vs)
    print(f"Compare B: {format_data(account_B)}.")

    #   Ask users for a guess
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the guess is correct
    # Check for no of followers
    acc_A_followers=account_A["follower_count"]
    acc_B_followers=account_B["follower_count"]
    if_correct=check_answer(guess,acc_A_followers,acc_B_followers)
    
    
    # clear the screen
    clear()

    # Give user feedback on their guess
    # Score tracking
    if if_correct:
        score+=1
        print(f"You're right, Your score is {score}")
    else:
        game_should_continue= False
        print(f"Sorry, You got it wrong, Your final score is {score}") 

    


