import art
import data
import random


def checker(guess, a, b):
    if guess == "a":
        if a > b:
            return True
        else:
            return False
    if guess == "b":
        if a < b:
            return True
        else:
            return False


def game():
    end = True
    score = 0
    while end:
        print(art.logo)
        if score != 0:
            print("\n" * 50)
            print(f"You are right! Current score : {score}")
        else:
            a = random.choice(data.data)
        b = random.choice(data.data)
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(art.vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        guess = input("Who has more followers on Instagram? Type 'A' or 'B' : ").lower()
        if checker(guess, int(a['follower_count']), int(b['follower_count'])):
            score += 1
            a = b
        else:
            print(f"Sorry, but your guess was wrong. Your final score is : {score}")
            end = False


game()
