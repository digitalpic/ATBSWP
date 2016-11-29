# Guess the number game!
import random
import time

print('Hi and Welcome to the Number Guessing Game.')
time.sleep(2)
print('You have 6 chances to guess a number between 1 and 20.')
time.sleep(2)
print('But first, what shall I call you?')
name = input() # Wait for the user's imput 
time.sleep(1)

print('Ok, ' + name + ', Hmm, I am thinking of a number in between 1 and 20')
secretNumber = random.randint(1, 20) # between 1 and 20
while True:
    try:
        for guessesTaken in range(1, 7): # Just 6 guesses
            print('Go ahead - take a guess.')
            guess = int(input()) # user input

            if guess < secretNumber: # if lower than
                print('That guess was too low.')
            elif guess > secretNumber: # If higher than
                print('That guess was too high.')
            else:
                break  # Guess the number correct and print to console

        if guess == secretNumber:
            print('Good job, ' + name + '! You guessed my number in ' +
                  str(guessesTaken) + ' guesses!')
        else:
            print('Nope. The number I was thinking of was ' +
                  str(secretNumber) + ' Too bad!')
    # TODO: These errors reset the counter (range) above.
    except (ValueError, TypeError):
        print(" Let's start over... Enter a 'number'...")
    else:
        break
