import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log_with_input(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print('2021-04-09')


@log_with_input('execute')
def now_custom():
    print('2021-04-09')


now()
print(now.__name__)

now_custom()
print(now.__name__)