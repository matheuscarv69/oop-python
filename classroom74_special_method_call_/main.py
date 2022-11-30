"""
20:55


Método Especial: __call__

callable é algo que pode ser executado com parênteses

Em classes normais, __call__ faz a instância de uma classe "callable"

"""


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, caller):
        print(f'{caller} Calling phone: {self.phone}')


call1 = CallMe('123123123')

call1(caller='Detonator')
