class Address:

    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city} - {self.state} is deleted')
