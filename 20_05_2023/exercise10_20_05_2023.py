# Create an algorithm that reads a product price and returns the new price with 5% discount.

product_price = float(input('What is the price product? R$'))

print('The new price with 5% discount is R${:.2f}.'.format(product_price-(product_price*0.05)))
