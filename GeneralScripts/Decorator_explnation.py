"""
        A test file for decorator
"""
import time

def double(x):
    return x * 2


def triple(x):
    return x * 3


def my_func(func, x):
    print(func(x))


def get_multiply_func(n):
    def multiply(x):
        return n * x

    return multiply


calc_double = get_multiply_func(2)
calc_triple = get_multiply_func(3)

print(calc_double(3))
print(calc_triple(3))


def dec(func):
    return 1


@dec
def double(x):
    return x * 2

print(double)
double = dec(double)


def calc_time(func):

    def wrapper(x):  # *args, **kwargs
        start = time.time()
        ref = func(x)  # *args, **kwargs
        print(time.time() - start)
        return ref
    return wrapper

@calc_time
def my_func(x):
    lst = []
    for i in range(1000):
        lst.append(i)

    time.sleep(x)
    return lst


@calc_time
def double(x):
    return x * 2
print(my_func)

my_func = calc_time(my_func)

print(double(2))