# Create a program that reads an integer and returns its multiplication table

integer = int(input('Type an integer: '))

print('-' * 12)
print('{} x {:2} = {}'.format(integer, 1, integer*1))
print('{} x {:2} = {}'.format(integer, 2, integer*2))
print('{} x {:2} = {:2}'.format(integer, 3, integer*3))
print('{} x {:2} = {}'.format(integer, 4, integer*4))
print('{} x {:2} = {}'.format(integer, 5, integer*5))
print('{} x {:2} = {}'.format(integer, 6, integer*6))
print('{} x {:2} = {}'.format(integer, 7, integer*7))
print('{} x {:2} = {}'.format(integer, 8, integer*8))
print('{} x {:2} = {}'.format(integer, 9, integer*9))
print('{} x {:2} = {}'.format(integer, 10, integer*10))
print('-' * 12)

