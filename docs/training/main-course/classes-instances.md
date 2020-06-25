# Be classy: Python Classes and Instances

Classes are the Python building block creating user-defined types in an object-oriented manner. Classes encapsulate data ('attributes') and appropriate functions ('methods'), which define the bahaviour of class-instances (i.e. objects of that class). Python supports 'composition' ("has-a"-relation) and (multiple-) 'inheritance' ("is-a"-relation) between classes/instances. In combination with 'method-overriding' and a special kind of 'polymorphism' (***Duck-Typing***), Python offers most of bunch of object-oriented features (Most, because Python doesn't really supports class privacy as explained below).
Classes itself are objects, as such define a state (e.g. the `__name__` attribute) and a behaviour (a set of methods) - the most common is the class-costructor, which creates instances of a class.

Let's start with a simple class.

## Simple class

Simple classe typically have instance-attributes and instance-methods.

1. instance attributes: 
    - each class instance has its own 'local' copy of its instance-atttributes  
    - instance-attributes are accessd using the `.`-dot operator:  Pseudo-syntax `<class-instance>.<instance-attribute>`
2. instance-methods: 
    - must be called with a class-instance
    - instance-methods are accessed using the `.`-dot operator: Pseudo-syntax `<class-instance>.<instance-method>(<params>)`
    - the 'class constructor' is named `__init__()`. The `__init__()`-method is not mandatory to create class-instances (that's the task of the [`__new__()`-method](https://docs.python.org/3/reference/datamodel.html?highlight=__init#object.__new__), which is implicitly there. But practically the `__init__()`-method is always necessary to initialize the instance-attributes. To be more precisely: A class-instatiation is a 2-step process 1. creating the class (`__new__()`)and 2. initialisation (`__init__()`). During a class-instantiation these 2-steps are implicitly performed by the interpreter.
    - a class can define a destructor-mehod called `__del__()`, to explicitly do some finalizer tasks e.g. close ressources opened by the class-instance. The destructor is never called explicitly by user-code, instead its is called by the interpreters garbage collector, when the reference count (see [Object Lifetime and Object Reference](objects.md)) of the class instance reaches 0. For more details see [__del__()](https://docs.python.org/3/reference/datamodel.html?highlight=__del#object.__del__).
    - every instance-method need an explicit *1.st*-parameter named `self`

***class definition example (1)***

``` python
>>> class A:pass
...
>>>
```

***class `__name__`- attribute***

```python
>>> A.__name__
'A'
>>>
```


***class definition (2)***  

``` python
>>> class A:
...     def __init__(self, name):  # class constructor
...          self.name = name      # instance-attribute
...     def getName(self):         # instance method
...         return self.name
... 
>>>
```
  
***class instantiation - attribute and method access***

``` python
>>> a1 = A('A')
>>> a1.name                # attribute-access using class-instance and '.'-dot operator
'A'
>>> a1.getName()           # method-access  using class-instance and '.'-dot operator
'A'
>>>  a.__class__.__name__  # class-attribute 
'A'
>>>
```

## Note on `self`-parameter 

During a instance-method call the python interpreter implicity converts (pseudocode)

    <class-instance-object>.<instance-method>(<param-1>, ... <param-n>)

into

    <class-object>.<instance-method>(<class-instance-object>, <param-1>, ..., <param-n>)

The `self`-argument is the class-instance-object iself. See also the section [Instance methods](https://docs.python.org/3/reference/datamodel.html?highlight=__del#the-standard-type-hierarchy) auf the Python docs.

The `self`-parameter is therefore similar to the `this`-pointer of C++ and Java:

1. Python `self`: Explicit 1.st parameter in every instance-method
2. C++ `this`-pointer: Implicit parameter to all member functions. It's a keyword holding a pointer to the current object 
3. Java `this`-reference: Implicit parameter of all member functions. It's a keyword holdung a reference to the current object

***Note:***
The name `self` is a convention , and could be changed, but it shouldn't, because it keeps's the code understandable.

## Class Privacy - private Attributes

Python doesen't provide any kind of 'access-specifiers' like e.g. C++ (`public`, `private`, `protected`) to control access to
attributes or methods. I.e. attributes and methods are 'public' accessible.

Python provides 2 weak forms of data-hiding (but no real protection by access-control)

1. 'private-by-convention': Attributes prefixed with a single underscore `_` should be regarded as a private attribute
2. 'private-by-lexical-substitition': Attributes prefixed with double underscores `__` like e.g. `__foo` will be implicitly renamed to `_classname__foo` by the interpreter. This textual substitution is called 'name-mangling'.

As can be seen the following example this 'protections' can be bypassed:

``` python
>>> class A:
...     def __init__(self, name):
...         self.name = name
...         self._name = name        # attribute 'private-by-convention'
...         self.__name = name       # attribute 'private-by-lexical-substitution'
...     def getName(self):
...         return self.name
...     def _getName(self):
...         return self._name
...     def __getName(self):
...         return self.__name
...
>>>
```

***usage***

```python
>>> a = A("ClassPrivacy")
>>> dir(a)
['_A__getName', '_A__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_getName', '_name', 'getName', 'name']
>>> a.name             # (1) public attribute
'ClassPrivacy'
>>> a._name            # (2) private-by-convention ==> still accessible
'ClassPrivacy'
>>> a.__name           # (3) private-by-lecical-convention ==> not accessible because it is not found
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__name'
>>> a.getName()        # (4) public method                       
'ClassPrivacy'
>>> a._getName()       # (5) private-by-convention ==> still accessible/callable
'ClassPrivacy'
>>> a.__getName()      # (6) private-by-lexical-convention ==> not accessible because it is not found
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__getName'
>>> a._A__name         # (7) bypass protection because you know the rule
'ClassPrivacy'
>>> a._A__getName()    # (8) bypass protection because you know the rule
'ClassPrivacy'
>>>
```

For more details please refer to [Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables)

## Inheritance ("is-a"-relation)

***Note on class privacy:***
As mentioned above, Python doesn't provide any real mechanism for class privacy, neither 'data-protection' nor 'data-hiding'. This also applies to class-inheritance. Inheritance is public by default, as a consequence all of the base-class attributes and methods are inherited by the derived-class


***class definition***  

``` python
>>> class B(A):                            # class 'B' inherhits from class 'A'
...     def __init__(self, name, number):  # class constructor
...         A.__init__(self, name)         # call base-class initialisation-method
...         self.number = number           # instance variable
...     def getNumber(self):               # instance methode
...         return self.number
... 
>>> 
```

***class instantiation***

``` python
>>> b = B('Inheritance', 100)
>>> b.name                                # attribute-access
'Inheritance'
>>> b.getName()                           # method-access
'Inheritance'
>>> b.number                              # attribute-access
100
>>> b.getNumber()                         # attribute-access     
100
>>>
```

## Multiple Inheritance

Python also supports multiple inheritance

***class definition*** 

``` python
>>> class A:
...     def __init__(self, name):
...         self.name = name
...     def getName(self):
...         return self.name
... 
>>>
>>> class Z:
...     def __init__(self, another_name):
...         self.another_name = another_name
...     def getAnotherName(self):
...         return self.another_name
... 
>>>
>>> class B(A,Z):   # multiple inheritance 
...     def __init__(self, name, another_name, number):
...         A.__init__(self, name)           # call base-class initialisation-method of class 'A'
...         Z.__init__(self, another_name)   # call base-class initialisation-method of class 'Z'
...         self.number = number
...     def getNumber(self):
...         return self.number
...
>>>
```

***class instantiation*** 

```python
>>> b = B('BaseClass_A', 'BaseClass_Z', 100)
>>> b.getNumber()
100
>>> b.getName()
'BaseClass_A'
>>> b.getAnotherName()
'BaseClass_Z'
>>> dir(b)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'another_name', 'getAnotherName', 'getName', 'getNumber', 'name', 'number']
>>>
```

***Note:***
The `dir(<object>`)- builtin function lists all names in the namespace of the given object. As can be seen above all defined names of all base-class are in the namespace of the derived class.

## Composition ("has-a"-relation)

Python also support composition, i.e. a class 'B' has an instance-attribute pointing to an instance-attribute of class 'A'

***class definitions***  

``` python
>>> class A:
...     def __init__(self, name):
...         self.name = name
...     def getName(self):
...         return self.name
... 
>>> class B:
...     def __init__(self, name, number):
...         self.a = A(name)               # create a class 'A' (calling the constructor of class 'A') instance and old a reference to it (class 'B' "has-a" an instance-attribute of class 'A'
...         self.number = number
...     def getNumber(self):
...         return self.number
...     def getName(self):
...         return self.a.getName()
... 
>>>
```

***class instantiation***

``` python
>>> b = B('Composition', 100)
>>> b.getName()     # (1): indirect access to instance-variable 'a'
'Composition'
>>> b.a.getName()   # (2): direct access to instance-variable 'a'
'Composition'
>>> b.a.name        # (3): direct access to instance-variable 'a'
'Composition'
>>> b.getNumber()
100
>>> 
```

## Class Attributes

As opposed to 'instance'-attributes 'class'-attributes are common to all class instances.

***class definition***

``` python
>>> class A:
...     count = 0
...     def __init__(self, name):
...         self.name = name
...         A.count += 1
... 
>>> 
```    

***class instantiation***

``` python
>>> a1 = A('A1')    # 1.st instance increments class-attribute
>>> a1.count
1
>>> a2 = A('A2')    # 2.nd instance increments class-attribute
>>> a2.count
2
>>> a1.count        # Note: both instances share the same attribute
2
>>>
>>> id(a1.count)
140201179340160
>>> id(a2.count)
140201179340160
>>>
```


## Class Properties

Ordinary Python instance-attributes are by default 'readable', 'writable' and 'deletable'. Python class properties ('property-attributes') are attributes with 'access-control', i.e. they can be designed to be 'readable', 'writeable' and 'deletable'. Python properties therefore are managed attributes. This is done with special `getter`-, `setter`- and `deleter`- methods which enables the properties to be accessed as ordinary atttributes (instead of a method-call).

***Usecase:***
Properties are a way of data encapusulation. Hiding ordinary attributes behind a 'property-interface/facade' introduces a level of indirection to the origin attribute. The origin attribute may change behind the scenes in keeping the user interface with the property-facade. The property can be seen as the user-interface, while the origin attribute is an implementation detail which is a subject to change. 

Python support two different ways of implementing properties:

1. 'lower-level' using `property()` builtin function
2. 'higher-level' using  `@propery`-decorator

The Python docs provide a good [property-example](https://docs.python.org/3/library/functions.html#property), with read-, write- and delete-access. For convenience this is simply copied here. 

***example using `property()`-builtin function***

``` python
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
```

usage

``` python
>>> p1 = C()
>>> p1.x = 1       # (1) set property value
>>> p1.x           # (2) get property value
1
>>> del p1.x       # (3) delete property
>>> p1.x = 11      # (4) re-create property
>>> p1.x
11
```

***example using the `@propery`-builtin decorator***
``` python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```

usage

``` python
>>> p1 = C()
>>> p1.x = 9       # (1) set property value
>>> p1.x           # (2) get property value
9
>>> del p1.x       # (3) delete property
>>> p1.x = 99      # (4) re-create property
>>> p1.x
99
>>>
```

***'readonly property example ***

The above example stripped-down to be read-only:

``` python
>>> class C:
...     def __init__(self, x):
...         self._x = x
...     @property
...     def x(self):
...         return self._x
... 
>>>
```

usage

```python
>>> a = C('foo')
>>> a.x                                   # (1) read access
'foo'
>>> a.x = 'bar'                           # (2) write access
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>> del a.x                              # (3) delete access
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't delete attribute
>>>  
```

***Note:***
Property 'x' is read-only, write- and delete-access fail.


## Duck Typing

Statically typed languages like C++ use virtual function for runtime polymorphism. Derived classes therefore override base-class functions retaining their signature. When base-class objects, which hold a derived class reference, call their base-class function, the runtime will virtual dispatch the derived-class function.
This allows programing on a abstract base-class level. But this is restricted to class-objects having an inheritance relationship.

Pythons polymorphism is based on 'duck typing', where the polymorphism is not based on common types, instead it is based on common behaviour (methods) and attributes of the objects itself. See Wikipedia article on [Duck typing](https://en.wikipedia.org/wiki/Duck_typing): "If it walks like a duck and it quacks like a duck, then it must be a duck" 

This enable more architecural freedom on the program/class-design, because class-hierarchies can be breaked down and allow more loosely coupled program-design, as David M. Beazley writes in his Book "Python Essential Reference (Fourth Edition)".


## Special Methods

### class methods

As opposed to instance-methods, class-methods operate on the class-object.

***Usecase:*** 
Python doesn't support method overloading like C++ or Java. Therefore multiple methods with the same name within a single class is not supported. As a consequence only a single class constructor (`__init__()`-method) can be defined. With 'class-method's it's possible to overcome this.

Python 'classc-methods' are defined using the `@sclassmethod`-decorator preceeding to the method-definition

*`@classmethod`-example*

``` python
>>> class ByteStringStore:
...     encoding = 'utf-8'
...     def __init__(self, bytestring):
...         self.bytestring = bytestring
...     @classmethod
...     def from_unicode(cls, unicodestring):
...         return cls(unicodestring.encode(cls.encoding)
... 
... )
... 
>>> a = ByteStringStore(b'abc')
>>> b= ByteStringStore.from_unicode('äöü')
>>> type(a)
<class '__main__.ByteStringStore'>
>>> type(b)
<class '__main__.ByteStringStore'>
>>> 

```

### Static Methods

Python static-methods neither work on class-instance-objects nor on class-objects (that's the task of 'instance-method' and 'class-methods'). Python 'static-methods' can best be compared to module-functions, defined in the namespace of a class, instead of a modules-namespace.

***Usecase:*** Python 'static-methods' can be used for (utility-)functions that logical link to a class, but do not work on the class or their instaances itself

Python 'static-methods' are defined using the `@staticmethod`-decorator preceeding to the method-definition

*`@staticmethod`-example*

```python
>>> class A:
...     @staticmethod
...     def mystaticmethod():
...         print('this is a staticmethod')
... 
>>> A.mystaticmethod()
this is a staticmethod
>>>
```

Python `@staticmethods` are the correspondents to C++ and Java staticmethods, see the Python docs for [`classmethod`](https://docs.python.org/3/library/functions.html#classmethod)

## Callable Classes

Callable classes are classes where the class-instances can simply be called as a function. Giving the class a callable-interface, their instances are callable. A class is made callable by defining a the special instance-method named `__call__()`).
 
 ***Usecase:***
 If different classes provide different instance-method names for the same functionality (e.g. `A.getName()` and `B.getMyName()`), the usage for the programmers is cumbersome. If they want to get the name from the objects on the one hand they have to call `a.getName()`and on the other hand `b.getMyName()`. Making the classes callable, gives them a uniform interface, the name for both class-instance can be fetched in the same manner, simply using the object-name following parenthesis: `a()` and `b()`.
 
 ***Definition of a callable class***
 
``` python
>>> class CallableClass:
...     name = None
...     def __init__(self, name):
...         CallableClass.name = name
...     def getName(self):
...         print('>>> calling normal instance-method: %s() <<<' % self.getName.__name__)
...         return CallableClass.name
...     def __call__(self):
...         print('>>> calling special instance-method: %s() <<<' % self.__call__.__name__)
...         return CallableClass.name
... 
>>>
```



***Usage of a callable instance*** 

``` python
>>> foo = CallableClass('foo')                        # (1) Create an instance of the callable class
>>> print('name = %s' % foo.getName())                # (2) use the 'standard'-class-interface instance-method 'getName()'
>>> calling normal instance-method: getName() <<<
name = foo
>>> print('name = %s' % foo())                        # (3) use the 'callable'-class-interface instance-method '__call__()'
>>> calling special instance-method: __call__() <<<
name = foo
>>> 
```


Let's give it a try

--8<--
lessons/customer.md
--8<--


## Class Decorators

Decorators are explained in detail [here](decorators.md). Here we just give a brief overview concerning decorating in the context of classes.

***Usecase***
Generally speaking a decorator is a 'wrappers' around functions or classes with the purpose of adding some functionality.
Wrappers are callable object, see [callable-class](#callable-classes).

So there are two parties in the decorating process:

1. the decorator
2. the object to be decorated

### Using a class as a decorator

In the following example we define a ***class*** as a decorator and define a ***function*** which is decorated with this 'class-decorator'.

***Class Decorator definition and function decoration***

``` python
>>> class MyDecorator:
...     def __init__(self, func):
...         self.func = func
...     def __call__(self, *args):
...         # put the additional functionalty here around the function
...         print('==> START calling %s()' % self.func.__name__)  # some output before the wrapped function is called
...         self.func(*args)                                      # call the wrapped-function
...         print('<== END calling %s()' % self.func.__name__)    # some output after the wrapped function is called
... 
>>> @MyDecorator
... def myfunc(x):
...     print('>>> INSIDE decorated function: %s<<<' % x)
... 
>>>
```

***function call***

``` python
>>> myfunc('decorator-example')
==> START calling myfunc()
>>> INSIDE decorated function: decorator-example<<<
<== END calling myfunc()
>>> 
```

***Note:***
Here the class-decorator was used to provide some additional output, when the 'decorated' function is called.

### Decorating a class

In the following example we define a ***function*** as a decorator and define a ***class*** which is decorated with this 'function-decorator'.

***Note:***
Here the decorator works on class-definition level, providing some additional funtionality around the class-definition. For sure a rather infrequent usecase which can be classified in some sense as meta-programming.

``` python
>>> def mydecoratorfunc(cls):
...     print('>>> A new class was born: %s' % cls)
...     return cls
... 
>>> @mydecoratorfunc
... class A: pass
... 
>>> A new class was born: <class '__main__.A'>
>>> 
```

## Class Testing

Python provides 2 builtin-function to identify/test the membership on class-instance-types.

1. `types()`: Identifies the concrete class of the class-instance
2. `isinstance()`: Testing the belonging to a certain type (along the class-hierarchy!)

```python
>>> class A(): pass
... 
>>> class B(A): pass
... 
>>> class C(): pass
... 
>>> a = A()
>>> b = B()
>>> c = C()
>>> type(a)
<class '__main__.A'>
>>> type(b)
<class '__main__.B'>
>>> type(c)
<class '__main__.C'>
>>> isinstance(a, A)
True
>>> isinstance(b, A)          # check along the inheritance-hierarchy
True
>>> isinstance(c, B)
False

```

## MetaClasses

It should be mentioned that Python also supports techniques for meta-programming, for example to create metaclasses. But this is subject to advanced courses.

## Further readings on classes

 Please refer to the Python docs about [Classes](https://docs.python.org/3/tutorial/classes.html).
 



  
