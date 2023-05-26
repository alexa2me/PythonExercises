# Create an algorithm that reads a phrase and returns:
# * How many times the letter "A" appears
# * In which position it appears for the first time
# * In which position it appears for the last time

phrase = str(input('Type a phrase: ')).strip()

phrase_upper = phrase.upper()
amount_of_a = phrase_upper.count('A')
first_time_a = phrase_upper.find('A')
last_time_a = phrase_upper.rfind('A')

print('The amount of A in the phrase is: {}.'.format(amount_of_a))
print('The first A appears in the position: {}.'.format(first_time_a))
print('The last A appears in the position: {}.'.format(last_time_a))
