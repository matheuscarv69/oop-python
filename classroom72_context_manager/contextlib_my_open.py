# Context Manager com função usando decorator

from contextlib import contextmanager


@contextmanager
def my_open(filepath, mode):
    try:
        print('Opening file')

        file = open(filepath, mode, encoding='utf8')

        """
        O context manager tem duas ações: abrir e fechar,
        No __enter__ usamos o return para retornar o arquivo
        Aqui vamos usar yield(isso torna a função um generator 
        de certa forma) para retornar o file.
        
        Apoio: https://pt.stackoverflow.com/questions/92921/para-que-serve-o-yield#:~:text=o%20yield%20faz%20parte%20do,mais%20escal%C3%A1vel%2C%20poupando%20mem%C3%B3ria%20principalmente.
        """
        yield file
    finally:
        print('Closing file')
        file.close()


with my_open('log_history_contextlib.txt', 'w') as file:
    file.write('Log 1 \n')
    file.write('Log 2 \n', 123)
    file.write('Log 3 \n')

    print('WITH', file)
