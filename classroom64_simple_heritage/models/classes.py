class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'{self.name} is talking...')


class Client(Person):
    def buy(self):
        print(f'{self.name} is buying...')


class Student(Person):
    def study(self):
        print(f'{self.name} is studying...')
