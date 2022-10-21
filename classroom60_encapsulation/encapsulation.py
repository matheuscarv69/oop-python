"""
Encapsulamento:

Modificadores de acesso: public, protected, private
Esses modificadores são diferentes em Python:
Temos:
_ -> fracamente private ou protected
__ -> fortemente private

Quando uma variável é fortemente private __var, ela
deixa de ser acessível fora do seu escopo.

Para exibi-la fora do escopo é preciso fazer o seguinte:

instanciaDaClasse._Classe__var
ex:
db._DataBase__datas

"""


class DataBase:

    def __init__(self):
        self.__datas = {}

    def create_client(self, identifier, name):
        if 'clients' not in self.__datas:
            self.__datas['clients'] = {identifier: name}
        else:
            self.__datas['clients'].update({identifier: name})

    def get_all_clients(self):
        print()
        for table_name, clients in self.__datas.items():
            print(f'{table_name}:')

            for key, client_name in clients.items():
                print(f'\t{key} :  {client_name}')

    def remove_client(self, identifier):
        del self.__datas['clients'][identifier]

    # end class


db = DataBase()
db.create_client(1, 'Axel')
db.create_client(2, 'Slash')
db.create_client(3, 'Bob Marley')

db.get_all_clients()

db.remove_client(2)

db.get_all_clients()

print()
print('Acessando uma variável fortemente privada')
print(db._DataBase__datas)
