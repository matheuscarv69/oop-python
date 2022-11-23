"""

__new__ e __init__ em classes Python

__new__ é o método responsável por criar e retornar o novo objeto.
Por isso, new recebe cls.

__new__ ❗️DEVE retornar o novo objeto❗️

-x-

__init__ é o método responsável por inicializar a instância.
Por isso, init recebe self.

__init__ ❗️NÃO DEVE retornar nada (None)❗️

-x-

object é a super classe de uma classe

"""


class A:

    # new é chamado antes de init por debaixo dos panos
    # Deve retornar uma instância da classe
    # Ordem de execução: new -> init
    # *args, **kwargs são usados pois, caso algum parâmetro seja definido
    # no __init__ ele deve ser repassado para o __new__
    # Usando *args, **kwargs evitamos de ter que repetir a mesma qtd de
    # parâmetros entre os métodos
    def __new__(cls, *args, **kwargs) -> object:
        print('Before to create instance')
        instance = super().__new__(cls)
        print('After to create instance')
        return instance

    def __init__(self, x) -> None:
        print('init is called')
        self.x = x

    # __repr__ é usado para representar para outro dev como o objeto
    # é representado
    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)