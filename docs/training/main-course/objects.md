# Python Objects: Understanding (the basics of) the Python Object Model

## Everything is an Object

In Python everything is an object:

Functions are objects, classes are objects, instances are objects, types are
objects, modules are objects, you name it: everything's an object. Even code
is an object:

``` python
>>> source = "lambda: 'Hello!'"
>>> code = compile(source, '', 'eval')
>>> type(code)
<class 'code'>
>>> isinstance(code, object)
True
>>> f = eval(code)
>>> f()
'Hello!'
>>>
```


An object is an entity encompassing the "data" and its acceptable operations.
The Python data model documentation
(<https://docs.python.org/dev/reference/datamodel.html>) describes:

"Every object has an ***identity***, a ***type*** and a ***value***. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity."

Often, Python objects are created and *named* immediately with an assignment.
Assigments introduce a *name* to refer to the object but don't create the
object:[^float-identity]

    :::python
    >>> a = 1.2  # new name a for new float object
    >>> b = 1.2  # new name b for new float object
    >>> c = a    # new name c for existing float object
    >>> type(a)
    <class 'float'>
    >>> type(b)
    <class 'float'>
    >>> type(c)
    <class 'float'>
    >>> id(a)        # (1)
    140026583519544  # (2) different identity than (1) ==> different object
    >>> id(b)
    140026583519592
    >>> id(c)        # (3) same identity as (1) ==> same object
    140026583519544
    >>> a is b
    False
    >>> a is c
    True
    >>>

[^float-identity]:
    Note though that `a = 1.2; b = 1.2; a is b` would actually yield `True`!
    This is due to identical float constants on the same line being stored as 
    one float constant, thus labeling the single float object with the names
    `a` and `b`
    (try `compile('a = 1.2; b = 1.2; a is b', '', 'exec').co_consts`).

But note that an object *needn't have* a name:

    :::python
    >>> l = [1, 2.0, lambda x: x]

In this example while the `list` does have a name ("l") none of its items has
one: Neither the 1st integer item nor the 2nd float item nor the 3rd anonymous
function item.

Python objects can be created e.g. by

 - instantiating built-in types
 - instantiating user-defined types (classes)
 - defining classes
 - defining functions
 - defining anonymous functions

You can create an instance of the most basic type `object` like this:

``` python
>>> object()
<object object at 0x7f33e1b9b0d0>
```

### Objects are First-Class
This means that all (named) objects are equal in the sense that they can be
treated equally: a function object can be an argument to another function,
a module object can be a list item, a class can be a dictionary value (or even
a dictionary key), ...

This allows for writing powerful constructs:
``` python
>> data = [42, 5.0, "some examples are more intelligent than others"]
>>> dispatcher = {                                
...     str: lambda x: x.strip(),  # we want strings stripped
...     int: lambda x: str(x**2),  # we want ints squared 
...     float: lambda x: str(-x)   # we want inverted floats
...     }
>>> print('|'.join(
...     dispatcher[type(d)](d) for d in data)
...     )
1764|-5.0|some examples are more intelligent than others
>>> 
```

### More characteristics of objects

1. The *identity* of an object never changes after creation (see above).
2. The *type* of an object never changes after creation.
3. The *type* of the object defines the allowed values and the acceptable
operations.
4. An objects is **mutable** if its *value* can be changed, **immutable**
otherwise.


## Immutable and Mutable Objects

The mutability/immutability of object-values is defined by its type:

 1. immutable types: `str`, `int`, `float`, `complex`, `tuple`, `frozenset`
 2. mutable types: `list`, `dict`, `set`, user-defined objects (classes)

### Examples: immutable types

Immutable type `int`:

    :::python
    >>> a = 1
    >>> id(a)
    140026581642624
    >>> a = 2       # assign name 'a' to a new object
    >>> id(a)
    140026581642656
    >>> a += 1
    >>> a
    3
    >>> id(a)       # a is now a name for another new object: immutable object 2 hasn't changed in-place
    140357021310400

Immutable type `float`:

    :::python
    >>> f1 = 1.2 
    >>> f2 = 1.2
    >>> f3 = f1     # (1) f3 is another name for the object named f1
    >>> id(f1)
    140026583519544
    >>> id(f2)
    140026583519592
    >>> id(f3)
    140026583519544
    >>> f1 = 1.3    # (2) the name f1 is now given to another object
    >>> f1
    1.3
    >>> f2
    1.2
    >>> f3          # (3) f3 is unaffected: it is still a name for the original object (1)
    1.2
    >>> id(f1)
    140026583519352
    >>> id(f2)
    140026583519592
    >>> id(f3)
    140026583519544
    >>> 


### Examples: mutable types

Mutable type `list`:

    :::python
    >>> l1 = [1, 2, 3]
    >>> l2 = l1      # (1) l2 is another name for the object named l1
    >>> id(l1)
    140026582652168
    >>> id(l2)
    140026582652168
    >>> l1[0] = 9    # (2) change a value of of l1
    >>> l1
    [9, 2, 3]
    >>> l2           # (3) the change (2) also effects the value of l2
    [9, 2, 3]
    >>> id(l1)
    140026582652168
    >>> id(l2)
    140026582652168
    >>> 
    >>> l1 =  [1, 2, 3]
    >>> l2 = l1
    >>> l1 += [4]  # extend mutable object
    >>> l1
    [1, 2, 3, 4]
    >>> l2
    [1, 2, 3, 4]
    >>> l1 is l2
    True
    >>> 


Mutable type `dict`:

    :::python
    >>> d1 = {1: 'one', 2: 'two'}
    >>> d2 = d1
    >>> d2[1] = 'three'  # create some confusion
    >>> d2
    {1: 'three', 2: 'two'}
    >>> d1
    {1: 'three', 2: 'two'}
    >>> 

## Object Lifetime and Object Reference

Every object that is created must be destroyed when it is no longer needed,
otherwise we run out of memory eventually. In Python objects aren't explicitly
destroyed but may be garbage-collected by the interpreter when they become
unreachable, i.e. they aren't referenced any more (by name or by other objects).

CPython implementation detail: CPython uses *reference counting*. Every object
carries the "in-use" information in a "reference count" which records the
number of references to this object. Remember, a variable is a name referencing
an object. An assignment of a name to an object establishes this reference -
during this step the reference count of the object is increased.

Conversely the object's reference count is decreased when the variable is
deleted (explicit using `del` or implicit by running out of scope) or
re-assigned to another object.

If the reference count of an objects is `0` the object is automatically destroyed by the garbage collector of the Python interpreter (not necessarily
immediately, so don't rely on it!).

You can watch these mechanisms using the `getrefcount()`-function of the Python
standard library module `sys`:

    :::python
    >>> import sys
    >>> l1 = ['cpython', 'does', 'refcounting']  # create named new list
    >>> sys.getrefcount(l1)
    2
    >>> id(l1)
    39141600
    >>> l2 = l1             # new name for existing object
    >>> id(l2)              # yes, it's the same object indeed
    39141600
    >>> sys.getrefcount(l1) # ==> refcount increased
    3
    >>> sys.getrefcount(l2)
    3
    >>> l3 = l1  # yet another new name for (=reference to) existing object
    >>> sys.getrefcount(l1)
    4
    >>> del l3               # delete name l3
    >>> sys.getrefcount(l1)  # ==> refcount of list object decreased
    3
    >>> l2 = object()        # assign name l2 to another object
    >>> sys.getrefcount(l1)  # ==> refcount of list object decreased
    2
    >>> 

**Remark:**
As you may have noted the reference count is higher than you might expect.
This is due to the fact that the `sys.getrefcount()`-function call also 
increases the object's reference count, as it needs to hold a reference to the 
object, too, while it is running.

