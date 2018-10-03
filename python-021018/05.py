def once(foo):
    from functools import wraps
    called = False
    res = None
    @wraps(foo)
    def wrapper(*args, **kwargs):
        nonlocal called
        nonlocal res
        if called:
            return res
        res = foo(*args, **kwargs)
        called = True
        return res
    return wrapper

@once
def func(a, b):
    from time import sleep
    sleep(1.25)
    print('a')
    return a + b

if __name__ == '__main__':
    print(func(2, 3))
    print(func(2, 3))