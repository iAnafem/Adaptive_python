import functools
import time
from datetime import datetime, timedelta


# Here is the pattern for creating a decorator:
#
# import functools
#
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee1():
    print("Whee!")


lol = my_decorator(say_whee1)

lol()


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


@not_during_the_night
def say_whee():
    print("Whee!")


say_whee()


def decorator1(func):
    @functools.wraps(func)
    def decorator1_wrapper(*args, **kwargs):
        print("Hello!, it's me, your decorator!")
        a = func(*args, **kwargs)
        print("Well, goodbuy ...")
        return a
    return decorator1_wrapper


@decorator1
def say_hello(name='Bastard'):
    return f"Hello!, call me {name}"


print(say_hello())


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting(name="Dorrisile", age=116)


def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)



countdown(5)


def memoize(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


class cached(object):
    def __init__(self, *args, **kwargs):
        self.cached_function_responses = {}
        self.default_max_age = kwargs.get("default_cache_max_age", timedelta(seconds=0))

    def __call__(self, func):
        def inner(*args, **kwargs):
            max_age = kwargs.get('max_age', self.default_max_age)
            if not max_age or func not in self.cached_function_responses or (
                    datetime.now() - self.cached_function_responses[func]['fetch_time']
                    > max_age
            ):
                if 'max_age' in kwargs:
                    del kwargs['max_age']
                res = func(*args, **kwargs)
                self.cached_function_responses[func] = {'data': res, 'fetch_time': datetime.now()}
            return self.cached_function_responses[func]['data']
        return inner


def new_decorator(func):
    @functools.wraps(func)
    def new_decorator_wrapper(*args, **kwargs):
        print("Hello! I'm working!")
        func(*args, **kwargs)
        print("stop working")
    return new_decorator_wrapper


def ololohsa(name, age):
    print(f'Hello, {name}. Are you {age}?')


new_decorator(ololohsa)('Dikiy', 32)


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
   выполнение декорируемой функции.
   """
    import datetime as dt
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = dt.datetime.now()
        res = func(*args, **kwargs)
        print(f'The function {func.__name__} performed {dt.datetime.now() - t}')
        return res

    return wrapper


@benchmark
def reverse_string(string):
    import time
    time.sleep(5)
    return ''.join(reversed(string))


print("тут --- ", reverse_string)

print(reverse_string('ololoshechkilolo'))


from functools import lru_cache


def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.time()

        result = func(*args, **kwargs)  # вызов декорированной функции

        elapsed = time.time() - t0
        name = func.__name__
        arg_1st = []
        if args:
            arg_1st.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_1st.append(', '.join(pairs))
        arg_str = ', '.join(arg_1st)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
@lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


print('fib(20) =', fib(20))