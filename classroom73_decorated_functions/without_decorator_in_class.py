"""
Função decoradoras e decoradores em classes
"""


class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'

        return class_repr


class Team(MyReprMixin):
    def __init__(self, name):
        self.name = name


class Planet(MyReprMixin):
    def __init__(self, name):
        self.name = name


brazil = Team('Brazil')
portugal = Team('Portugal')

earth = Planet('Earth')
mars = Planet('Mars')

print(brazil)
print(portugal)

print(earth)
print(portugal)
