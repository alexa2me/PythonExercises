# Create an algorith that reads a car speed and return a message if the speed is above 80Km/h
# and the price of the fine: R$7.00/km

speed = float(input('What is your speed? '))

if speed > 80:
    fine = (speed - 80) * 7
    print('You are above 80Km/h and your fine is R${:.2f}. Slow down next time.'.format(fine))
print('Have a nice day, drive safe!')
