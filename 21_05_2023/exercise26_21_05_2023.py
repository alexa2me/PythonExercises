# Create an algorithm that reads a full name and returns the first and last name separately.

full_name = str(input('What is your full name? ')).strip().split()

print('First name: {}\nLast name: {}'.format(full_name[0], full_name[-1]))
