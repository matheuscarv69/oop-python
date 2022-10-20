"""
Class Method é um método que pertence a entidade classe,
pode-se usá-lo independente de uma instância da classe.

ex: Um método que cria uma Pessoa através do ano de nascimento
"""


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

    #  end class


people1 = People.create_people_by_birth_year(name='Roger', birth_year=1969)
print(people1.age)
print(people1.get_birth_year())
