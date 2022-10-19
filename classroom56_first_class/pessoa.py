# Lib para pegar o ano atual
from datetime import datetime


class Pessoa:
    # Pega o ano atual
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    # __init__ é semelhante ao construtor padrão de Java/Kotlin
    def __init__(self, name, birth_year, eating=False, talking=False):
        self.name = name
        self.birth_year = birth_year
        self.eating = eating
        self.talking = talking

    def to_talk(self, theme):
        if self.talking == True:  # self.talking is right
            print(f'{self.name} is already talking')
            return

        print(f'{self.name} is talking about {theme}.')

    def to_eat(self, food):
        if self.eating == True:  # self.eating is right
            print(f'{self.name} is already eating')
            return

        print(f'{self.name} is eating {food}. ')

    def get_age(self):
        return self.current_year - self.birth_year
