from pessoa import Pessoa

axel = Pessoa(name='Axel', birth_year=1962, talking=True)
slash = Pessoa(name='Slash', birth_year=1965)

axel.to_talk('Java')
slash.to_talk('Python')

print()
print(f'{axel.name} is {axel.get_age()} years old')
print(f'{slash.name} is {slash.get_age()} years old')

