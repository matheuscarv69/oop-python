from Client import Client

client_1 = Client('Luiz', 48)
client_1.insert_address(city='Belo Horizonte', state='MG')

print(f"{client_1.name}'s Address:")
client_1.list_address()

"""
del está sendo utilizado para excluir o objeto client_1 e verificar
que o address criado no insert_address deixa de existir quando 
o client_1 é apagado 
"""
del client_1

print()

client_2 = Client('Maria', 55)
client_2.insert_address(city='Salvador', state='BA')
client_2.insert_address(city='Rio de Janeiro', state='RJ')

print(f"{client_2.name}'s Address:")
client_2.list_address()

del client_2

print()

client_3 = Client('João', 19)
client_3.insert_address(city='São Paulo', state='SP')

print(f"{client_3.name}'s Address:")
client_3.list_address()

del client_3

print()
print()

client_4 = Client('Kratos - O Bom de Guerra', 1909)
client_4.insert_address(city='Sparta', state='Olympus')

print(f"{client_4.name}'s Address:")
client_4.list_address()

print()
print('O Carbage Collector do Python ao fim da execução limpa da memória os objetos não excluídos com o del')
