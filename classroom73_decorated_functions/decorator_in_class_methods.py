"""
Função decoradoras e decoradores em classes
"""


def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} - ({class_dict})'

        return class_repr

    cls.__repr__ = my_repr

    return cls


def is_my_planet(method):
    def internal(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Earth' in result:
            return 'You are at home'

        return result
    return internal


@add_repr
class Team:
    def __init__(self, name):
        self.name = name


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

    @is_my_planet
    def to_speak_name(self):
        return f'This planet is called {self.name}'


brazil = Team('Brazil')
portugal = Team('Portugal')

earth = Planet('Earth')
mars = Planet('Mars')

print(brazil)
print(portugal)

print(earth)
print(portugal)

print()

print(earth.to_speak_name())
print(mars.to_speak_name())
