# Create an algorithm that asks a distance in kilometers and return the price of the ticket,
# R$0.50 per Km for a trip until 200Km and R$0.45 for trips more distant than 200Km.

distance = float(input('Tell me the distance of your trip in Km: '))

# ticket_price = distance * 0.5 if distance <= 200 else distance * 0.45

if distance <= 200:
    ticket_price = distance * 0.5
else:
    ticket_price = distance * 0.45
print('The distance of your trip is {} and your ticket will cost R${:.2f}'.format(distance, ticket_price))
