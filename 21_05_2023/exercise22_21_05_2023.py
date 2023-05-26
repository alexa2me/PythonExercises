# Create an algorithm that reads a number between 0 and 9999 and returns each digit separated
# as the units, tens, hundreds and thousands.

number = int(input('Type the number: '))

units = number // 1 % 10
tens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000 % 10

print('Units: {}\nTens: {}\nHundreds: {}\nThousands: {}'.format(units, tens, hundreds, thousands))
