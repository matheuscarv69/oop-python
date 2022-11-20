"""

Associação - Usa | Agregação - Tem | Composição - É dono

Herança - Um objeto herda caracteristica de outro

"""
from models.classes import Client, Student

client = Client('Luwis', 39)
client.talk()
client.buy()

print()

student = Student('Max', 23)
student.talk()
student.study()
