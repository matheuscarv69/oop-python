"""
Static Methods é um método que pode ser chamado independente da
instância da classe.

Diferente de um Class Method, o Static Method não precisa receber
como parâmetro o 'self' ou a referência da classe 'cls', pois ele
é independente. Ele pode receber parâmetros.

ex: Um método que gere um Id
"""
from random import randint


class People:
    current_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def get_birth_year(self):
        print(f'Age - {self.current_year - self.age}')

    # class method, it is reference of class
    # cls = class, is traditional name of param
    @classmethod
    def create_people_by_birth_year(cls, name, birth_year):
        # cls accessing class property 'current_year' like a java class with final properties
        age = cls.current_year - birth_year

        return cls('name', age)

    @staticmethod
    def generate_id():
        random_number = randint(1000, 19999)
        return random_number

    #  end class


people1 = People.create_people_by_birth_year(name='Roger', birth_year=1969)
print(people1.age)
print(people1.get_birth_year())

# usando o static method
print(f'ID - {People.generate_id()}')
# também é possível usar o static method pela instância
print(f'ID - {people1.generate_id()}')
