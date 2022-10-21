class Pen:
    def __init__(self, brand):
        self.__brand = brand

    def write(self):
        print('Pen is writing.')

    @property
    def brand(self):
        return self.__brand
