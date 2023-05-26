# Create a program that reads how much money a person has in its wallet and returns
# how many dollars it's possible to buy, U$$ 1 = R$3,27

money = float(input('How much money do you have? R$'))

print('With R${} you can buy about U$${:.2f}'.format(money, money/3.27))

