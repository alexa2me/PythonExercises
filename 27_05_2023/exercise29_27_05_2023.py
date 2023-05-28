# Create an algorithm to ask the user for a number and returns if the number is even or odd.

number = int(input('Tell me a number: '))

if number % 2 == 0:
    print('The number {} is even!'.format(number))
else:
    print('The number {} is odd!'.format(number))
