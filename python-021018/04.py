def stopwatch(foo):
    from functools import wraps
    @wraps(foo)
    def timer(*args, **kwargs):
        from time import time
        print('`{:s}` started'.format(foo.__name__))
        t0 = time()
        res = foo(*args, **kwargs)
        t1 = time()
        print('`{:s}` finished in {:.2f}s'.format(foo.__name__, t1 - t0))
        return res
    return timer

@stopwatch
def func(a, b):
    from time import sleep
    sleep(1.25)
    return a + b

if __name__ == '__main__':
    func(2, 3)