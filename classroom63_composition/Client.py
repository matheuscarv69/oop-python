from Address import Address


class Client:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = []

    def insert_address(self, city, state):
        self.address.append(
            Address(city, state)
        )

    def list_address(self):
        for address in self.address:
            print(f'\t{address.city} - {address.state}')

    def __del__(self):
        print(f'{self.name} is deleted')