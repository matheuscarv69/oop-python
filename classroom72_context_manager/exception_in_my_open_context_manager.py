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


class MyOpen:

    def __init__(self, filepath, mode):
        print("INIT")

        self.filepath = filepath
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Opening file')
        self._file = open(self.filepath, self.mode, encoding='utf8')

        return self._file

    """
    O método __exit__ receberá a classe de exceção, a exceção e o
    traceback. Se ele retornar True, exceções no with serão suprimidas.
    """

    def __exit__(self, class_exception, exception_, traceback_):
        print('Closing file')
        print("EXIT\n")

        self._file.close()

        print('Exception Class: ', class_exception)
        print('Exception: ', exception_)
        print('Traceback: ', traceback_)

        # A exceção deixa de ser lançada quando o __exit__ retorna True
        return True


# o método __init__ é chamado ao criar uma instância da classe
instance = MyOpen('log_history.txt', 'w')

# o método __enter__ atribui o seu retorno à variável file
with instance as file:
    file.write("Log info: 1 \n")
    file.write("Log info: 2 \n", 123)  # deve dar erro
    file.write("Log info: 3 \n")

    print("WITH", file)
