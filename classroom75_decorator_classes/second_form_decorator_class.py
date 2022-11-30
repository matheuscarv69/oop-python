# Decorator Classes

class Multiply:

    # step 3
    def __init__(self, multiplier):
        print('INIT')
        self._multiplier = multiplier

    # step 4 - agora o call que recebe a função
    def __call__(self, func):
        # step 5 - criamos uma função interna para repassar os args e kwargs para a função decorada
        def internal(*args, **kwargs):
            result = func(*args, **kwargs)

            return result * self._multiplier

        # step 6 - retorna a referência da função interna
        return internal


# Isso é o mesmo que Multiply()(), internamente o python já executa a classe
@Multiply(10) # step 2
def to_sum(x, y):
    return x + y


two_more_for = to_sum(2, 4) # step 1
print(two_more_for)
