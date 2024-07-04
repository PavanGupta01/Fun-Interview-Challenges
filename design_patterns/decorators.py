import functools


def logger(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        print("Before function call")
        x = function(*args, **kwargs)
        print("Post function call")
        return x

    return inner


@logger
def sum(a: int, b: int):
    return a + b


print(sum(10, 20))
