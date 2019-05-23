def debug(func):
    from functools import wraps
    """Print the function signature and return value"""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


def get_size(func):
    """Print the returned data structure and its size in bytes"""
    from functools import wraps
    from sys import getsizeof

    @wraps(func)
    def wrapper(*args):
        print("Data structure: ", func(*args))
        print("Structure size is", getsizeof(func(*args)), "bytes")
    return wrapper


class CountCalls:
    def __init__(self, func):
        from functools import update_wrapper
        update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    from functools import wraps
    @wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


def cache(func):
    """Keep a cache of previous function calls (It's functools.lru_cache analog"""
    from functools import wraps
    @wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


@cache
@CountCalls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(20))
print(fibonacci(8))
