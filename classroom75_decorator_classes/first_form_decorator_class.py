# Decorator Classes

class Multiply:

    # step 2
    def __init__(self, func):
        print('INIT')
        self.func = func
        self._multiplier = 10

    # step 3
    def __call__(self, *args, **kwargs):
        print(args, kwargs)

        # step 4 - calling function passed in init method by decorator
        result = self.func(*args, **kwargs)

        # step 5 - return result
        return result * self._multiplier


@Multiply
def to_sum(x, y):
    return x + y


two_more_for = to_sum(2, 4)  # step 1
print(two_more_for)  # step 6 - printing result getting in step 5
