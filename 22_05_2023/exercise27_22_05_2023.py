import random

# Create an algorith that makes the computer "thinks" about a number between 0 and 5
# and asks the user to guess the chosen number, then returns to the user if the guess
# was right or wrong.

number = random.randrange(0, 5)
guess = int(input('What is your guess? '))

if guess == number:
    print('The number was {}, so you win, insolent human!'.format(number))
else:
    print('Well... The number was {}, so you lose, insolent human! (obviously)'.format(number))


