"""
Agregação

Basicamente uma classe não pode existir sem algo que ela dependa:
Ex.:

Um carro não funciona sem motor.
Uma casa precisa de uma porta para se entrar

"""

from Cart import Cart
from Product import Product

product_1 = Product(name='T-short', price=50)
product_2 = Product(name='Iphone', price=10000)
product_3 = Product(name='Mug', price=15)

cart = Cart()
cart.insert_product(product_1)
cart.insert_product(product_2)
cart.insert_product(product_3)

print(f'List Products in Cart:')
cart.list_product()

print()
print(f'Sum total: R${cart.sum_total():.2f}')
