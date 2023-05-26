# Create an algorithm that reads the number of days a car has been rented
# and the number of kilometers driven.
# The car costs R$60,00 a day and R$0.15 per kilometer driven.

days = int(input('How many days was the car rented for? '))
kilometers = float(input('How many kilometers have been driven? '))

print('The amount to be paid is R${:.2f}'.format((days*60)+(kilometers*0.15)))
