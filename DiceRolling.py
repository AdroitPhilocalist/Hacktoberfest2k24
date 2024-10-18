import random

def roll_dice():
    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Return the result as a tuple
    return die1, die2

def main():
    print("Rolling the dice...")
    die1, die2 = roll_dice()
    print(f"You rolled a {die1} and a {die2}!")
    print(f"Total: {die1 + die2}")

    # Check if the user wants to roll again
    while input("Do you want to roll again? (y/n): ").lower() == 'y':
        die1, die2 = roll_dice()
        print(f"You rolled a {die1} and a {die2}!")
        print(f"Total: {die1 + die2}")

main()
