import time
import logging

def profile(func):
    def wrap(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
#        logging.info(time.time() - started_at)
        print(time.time() - started_at)
        return result

    return wrap

def log_func_calls(log_id):
    def outer_wrap(func):
        def wrap(*args, **kwargs):
            print("{} Inside: {}".format(log_id, func.__name__))
            result = func(*args, **kwargs)
            print("{} Exit: {}".format(log_id, func.__name__))
            return result
        return wrap
    return outer_wrap

@profile
def foo(a, b):
    print(a, b)
    pass

@log_func_calls('TEST')
def foo_1(a, b):
    print(a, b)
    pass
foo(1, [2])
foo_1(1, [2])
