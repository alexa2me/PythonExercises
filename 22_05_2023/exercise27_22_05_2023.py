from random import randrange
from time import sleep

# Create an algorith that makes the computer "thinks" about a number between 0 and 5
# and asks the user to guess the chosen number, then returns to the user if the guess
# was right or wrong.

number = randrange(0, 5)
print('-=-' * 20)
print('I am going to think about a number... Try to guess...')
print('-=-' * 20)

guess = int(input('What is your guess from 0 to 5? '))
print('Processing...')
sleep(2)

if guess == number:
    print('The number was {}, so you win, insolent human!'.format(number))
else:
    print('Well... The number was {}, so you lose, insolent human! (obviously)'.format(number))


