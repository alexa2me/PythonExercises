# Create an algorithm that receive 3 numbers and returns which one is the biggest and the smallest.

number_1 = float(input('Tell me the first number: '))
number_2 = float(input('Tell me the second number: '))
number_3 = float(input('Tell me the third number: '))

if number_2 < number_1 < number_3:
    print('The biggest number is {} and the smallest one is {}.'.format(number_3, number_2))
elif number_3 < number_1 < number_2:
    print('The biggest number is {} and the smallest one is {}.'.format(number_2, number_3))
elif number_1 < number_2 < number_3:
    print('The biggest number is {} and the smallest one is {}.'.format(number_3, number_1))
elif number_3 < number_2 < number_1:
    print('The biggest number is {} and the smallest one is {}.'.format(number_1, number_3))
elif number_1 < number_3 < number_2:
    print('The biggest number is {} and the smallest one is {}.'.format(number_2, number_1))
else:
    print('The biggest number is {} and the smallest one is {}.'.format(number_1, number_2))
