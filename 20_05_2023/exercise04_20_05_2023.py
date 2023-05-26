# Create a program that reads a number and shows its double, triple and square root

number = int(input('Type a number: '))

print('The double is {}, the triple is {} and the square root is {:.2f}.'.format(number*2, number*3, number**(1/2)))
