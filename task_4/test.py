# просто сохраненный вариант, который написан не мной

def val_checker(check_fn):
    def _decorator(original_func):
        def wrapper(*args, **kwargs):
            if all(map(check_fn, (*args, *kwargs.values()))):
                return original_func(*args, **kwargs)
            raise ValueError('Wrong argument value in %s %s' % (args, kwargs,))
        return wrapper
    return _decorator
