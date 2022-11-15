class Cart:

    def __init__(self):
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def list_product(self):
        for product in self.products:
            print(f'\t{product.name}: R$ {product.price:.2f}')

    def sum_total(self):
        total = 0

        for product in self.products:
            total += product.price

        return total
