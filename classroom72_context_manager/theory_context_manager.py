"""
 Context Manager com classes - Criando e Usando gerenciadores de contexto

 Você pode implementar seus próprios protocolos apenas implementando os
 dunder methods que o Python vai usar.

 Isso é chamado de Duck typing.

 Um conceito relacionado com tipagem dinâmica onde o Python não
 está interessado no tipo, mas se alguns métodos existem no seu objeto
 para que ele funcione de forma adequada.

 Duck Typing:
 Quando vejo um pássaro que caminha como um pato, nada como
 um pato e grasna como um pato, eu chamo aquele pássaro de pato.

 Para criar um context manager, os métodos __enter__ e __exit__
 devem ser implementados.

 O método __exit__ receberá a classe de exceção, a exceção e o
 traceback. Se ele retornar True, exceção no with será
 suprimidas.

 Ex:
 with open('aula149.txt', 'w') as arquivo:
     ...
"""


class MyContextManager:

    def __init__(self):
        print("INIT")

    def __enter__(self):
        print("ENTER")
        return 1234

    def __exit__(self, class_exception, exception_, traceback_):
        print("EXIT")


# o método __init__ é chamado ao criar uma instância da classe
instance = MyContextManager()

# o método __enter__ atribui o seu retorno à variável some_thing
with instance as some_thing:
    print("WITH", some_thing)
