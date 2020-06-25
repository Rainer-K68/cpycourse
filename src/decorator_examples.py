def trace(func):
    # create a wrapper function...
    def _wrapper(*args, **kwargs):
        # ...that prints entry to and exit from the wrapped function,
        # with function name, arguments and result...
        print('--> {func}(args={args}, kwargs={kwargs})'.format(
            func=func.__name__, args=args, kwargs=kwargs))
        result = func(*args, **kwargs)
        print('<-- {func} -> {result}'.format(
            func=func.__name__, result=result))
    # ...and return the wrapper for use instead of the original function
    return _wrapper

@trace
def inc(x):
    """Return x increased by 1.
    """
    return 1

print(inc.__doc__)
inspect.signature(inc)
 



def trace(func):
    # create a wrapper function...
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        # ...that prints entry to and exit from the wrapped function,
        # with function name, arguments and result...
        print('--> {func}(args={args}, kwargs={kwargs})'.format(
            func=func.__name__, args=args, kwargs=kwargs))
        result = func(*args, **kwargs)
        print('<-- {func} -> {result}'.format(
            func=func.__name__, result=result))
    # ...and return the wrapper for use instead of the original function
    return _wrapper

@trace
def inc(x):
    """Return x increased by 1.
    """
    return x + 1

print(inc.__doc__)
inspect.signature(inc)
 

class Increaser:
    def __init__(self, increment=1):
        self.increment = increment
    @trace
    def inc(self, x):
        """Return x increased by increment init argument.
        """
        return x + self.increment

inc = Increaser(3)
inc.inc(10)

print(inc.inc.__doc__)
inspect.signature(inc.inc)


class Registry:
    _registered_classes = []
    
    @classmethod
    def register(cls, register_cls):
        cls._registered_classes.append(register_cls)
    
    @classmethod
    def registered_classes(cls):
        return cls._registered_classes

register = Registry.register
registry = Registry()

@register
class MyClass1:
    pass

@register
class MyClass2:
    pass

registry.registered_classes()
    

def traced(cls=None, entry=True, exit=True):
    if entry and exit:
        def trace(func):
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                print('--> {func}(args={args}, kwargs={kwargs})'.format(
                    func=func.__name__, args=args, kwargs=kwargs))
                result = func(*args, **kwargs)
                print('<-- {func} -> {result}'.format(
                   func=func.__name__, result=result))
            return _wrapper
    
    elif entry:
        def trace(func):
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                print('--> {func}(args={args}, kwargs={kwargs})'.format(
                    func=func.__name__, args=args, kwargs=kwargs))
                result = func(*args, **kwargs)
            return _wrapper
    
    elif exit:
        def trace(func):
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                print('<-- {func} -> {result}'.format(
                   func=func.__name__, result=result))
            return _wrapper
    else:
        trace = None
    
    
    def decorate(cls):
        if trace is not None:
            for (name, method) in inspect.getmembers(cls):
                if not name.startswith('__'):
                    wrapped = trace(method)
                    setattr(cls, name, wrapped)
        return cls
    
    return decorate


class FruitSalad:
        
    def __init__(self):
        self.fruits = {}
    
    def add(self, fruit, weight):
        if fruit not in self.fruits:
            self.fruits[fruit] = weight
        else:
            self.fruits[fruit] += weight


fruit_salad = FruitSalad()
fruit_salad.add('apple', '500')
fruit_salad.add('orange', '800')


@traced()
class FruitSalad:
        
    def __init__(self):
        self.fruits = {}
    
    def add(self, fruit, weight):
        if fruit not in self.fruits:
            self.fruits[fruit] = weight
        else:
            self.fruits[fruit] += weight

fruit_salad = FruitSalad()
fruit_salad.add('apple', '500')
fruit_salad.add('orange', '800')


@traced(entry=False)
class FruitSalad:
        
    def __init__(self):
        self.fruits = {}
    
    def add(self, fruit, weight):
        if fruit not in self.fruits:
            self.fruits[fruit] = weight
        else:
            self.fruits[fruit] += weight

fruit_salad = FruitSalad()
fruit_salad.add('apple', '500')
fruit_salad.add('orange', '800')


def traced(cls=None, *, entry=True, exit=True):
    if entry and exit:
        def trace(func):
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                print('--> {func}(args={args}, kwargs={kwargs})'.format(
                    func=func.__name__, args=args, kwargs=kwargs))
                result = func(*args, **kwargs)
                print('<-- {func} -> {result}'.format(
                   func=func.__name__, result=result))
            return _wrapper
    
    elif entry:
        def trace(func):
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                print('--> {func}(args={args}, kwargs={kwargs})'.format(
                    func=func.__name__, args=args, kwargs=kwargs))
                result = func(*args, **kwargs)
            return _wrapper
    
    elif exit:
        def trace(func):
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                print('<-- {func} -> {result}'.format(
                   func=func.__name__, result=result))
            return _wrapper
    else:
        trace = None
    
    def decorate(cls):
        if trace is not None:
            for (name, method) in inspect.getmembers(cls):
                if not name.startswith('__'):
                    wrapped = trace(method)
                    setattr(cls, name, wrapped)
        return cls
    
    
    if cls is None:
        # called with arguments
        return decorate
    else:
        # invoked without arguments
        return decorate(cls)

@traced
class FruitSalad:
        
    def __init__(self):
        self.fruits = {}
    
    def add(self, fruit, weight):
        if fruit not in self.fruits:
            self.fruits[fruit] = weight
        else:
            self.fruits[fruit] += weight

fruit_salad = FruitSalad()
fruit_salad.add('apple', '500')
fruit_salad.add('orange', '800')




