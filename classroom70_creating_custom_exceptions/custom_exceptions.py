"""
 Criando Exceptions em Python Orientado a Objetos
 Para criar uma Exception em Python, você só
 precisa herdar de alguma exceção da linguagem.

 A recomendação da doc é herdar de Exception.
 https://docs.python.org/3/library/exceptions.html

 Criando exceções (comum colocar Error ao final)
 Levantando (raise) / Lançando (throw) exceções
 Relançando exceções
 Adicionando notas em exceções (3.11.0)
"""


class MyError(Exception):
    ...


class OtherMyError(Exception):
    ...


# raise my custom exception
def raise_my_error():
    exception = MyError('Hi! I am an error', 'The Exception class receive an args with parameter')
    raise exception


try:
    raise_my_error()
except (MyError, ZeroDivisionError) as error:
    print(f'Error raised - {MyError.__name__} : {error}')

    # Re raise an new Exception
    other_my_error = OtherMyError('Hello guy, I am an other error')
    raise other_my_error
