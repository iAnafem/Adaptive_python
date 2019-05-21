def get_size(func):
    from functools import wraps
    from sys import getsizeof

    @wraps(func)
    def wrapper(*args):
        print("Data structure: ", func(*args))
        print("Structure size is", getsizeof(func(*args)), "bytes")
    return wrapper


@get_size
def create_structure(_type, *args):
    if _type == 1:
        return {_key: value for _key, value in zip(range(100), args)}
    elif _type == 2:
        return tuple(args)
    elif _type == 3:
        return list(args)
    else:
        return set(args)


create_structure(1, "Dude", "LOL", "It's really works!")
create_structure(2, "Dude", "LOL", "Really works!")
create_structure(3, "Dude", "LOL", "Really works!")
create_structure(4, "Dude", "LOL", "Really works!")
