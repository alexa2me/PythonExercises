# Create an algorithm that reads a person full name and returns:
# * The name in all capital letters
# * The name in all lowercase letters
# * The amount of letters in total without counting spaces
# * The amount of letters of the first name

name = str(input('What is your name? '))

separated_name = name.split()
united_name = ''.join(separated_name)

print('Name in all capital letters: {}'.format(name.upper()))
print('Name in all lowercase letters: {}'.format(name.lower()))
print('Amount of letters without counting the spaces: {}'.format(len(united_name)))
print('Amount of letter of the first name: {}'.format(len(separated_name[0])))
