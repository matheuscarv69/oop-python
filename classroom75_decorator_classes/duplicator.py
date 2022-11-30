class Duplicator:
    def __init__(self, func):
        self.func = func
        self._duplicator = 2
        print('1 - Running Init method at Duplicator Class - Decorator Class ')
        print(f'1 - func: {func} \n')

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)

        print(f'3 - Receiving args: {args} to function: to_sum')
        print(f'3 - Executing func in call method: self.func(*args, **kwargs)')

        return result * self._duplicator


@Duplicator
def to_sum(x, y):
    print(f'2 - Executing to sum for to pass args ({x},{y}) to call method in Decorator class \n')
    return x + y


duplicator_result = to_sum(2, 4)

print()
print('Duplicated result:', duplicator_result)
