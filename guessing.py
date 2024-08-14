import random
import sys

def guessNumber():
    print("I am thinking of a number between 1 and 20")
    
    player = int(input("Take a guess: "))
    computer = random.randint(1, 20)
    
    if player == computer:
        print("Good job")
    elif player < computer:
        print(f"Your guess is too low, computer guess is {computer}")
    else: 
        print(f"Your guess is too high, computer guess is {computer}")
    
    return input("\nWill you be interested in playing again? (y/n)\n").lower()

count = 0
while True:
    count += 1
    play_again = guessNumber()
    
    if play_again != 'y':
        print(f"\nYou have played {count} time(s)")
        sys.exit()


guessNumber()