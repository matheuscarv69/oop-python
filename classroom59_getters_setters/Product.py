class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def give_discount(self, percent):
        value = self.price - (self.price * (percent / 100))
        return value

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        self._name = name

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))

        self._price = value

    # end class


product1 = Product('T-shirt', 50)
new_price = product1.give_discount(10)

product1.name = 'Jacket'

print(f'Product: {product1.name}: R$ {product1.price:.2f}')
print(f'Applying Discount: {product1.name}: R$ {new_price:.2f}')

print()

product2 = Product('Mug', 15)
new_price2 = product2.give_discount(10)

print(f'Product: {product2.name}: R$ {product2.price:.2f}')
print(f'Applying Discount: {product2.name}: R$ {new_price2:.2f}')
