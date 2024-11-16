import art
import data
import random


game_over = False
a = random.randint(0, len(data) - 1)
score = 0

while not game_over:
    b = random.randint(0, len(data) - 1)
    
    # Ensure A and B are different
    while a == b:
        b = random.randint(0, len(data) - 1)
    
    print(f"Compare A: {data[a]['name']}, {data[a]['description']}, from {data[a]['country']}.")
    print(f"Compare B: {data[b]['name']}, {data[b]['description']}, from {data[b]['country']}.")
    
    answer = input("Choose A or B: ").upper()
    
    if data[a]['follower_count'] > data[b]['follower_count'] and answer == 'A':
        score += 1
        print(f"Correct! Current score: {score}")
    elif data[a]['follower_count'] < data[b]['follower_count'] and answer == 'B':
        score += 1
        print(f"Correct! Current score: {score}")
    else:
        print(f"You lost! Final score: {score}")
        game_over = True
    
    # Set A to be the last selection for the next round
    a = b
